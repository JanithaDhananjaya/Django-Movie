from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MovieInfo
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    all_movies = MovieInfo.objects.all()
    return render(request, "MovieReviewer/index.html", {'Movies': all_movies})


def addMovie(request):
    return render(request, "MovieReviewer/add_movie.html")


def submission(request):
    print("add new movie action works"),
    movie_name = request.POST["movie_name"]
    movie_type = request.POST["movie_type"]
    movie_review = request.POST["movie_review"]
    movie_release_date = request.POST["movie_release_date"]
    movie_detail = request.POST["movie_detail"]

    movie_info = MovieInfo(movie_name=movie_name, movie_type=movie_type, movie_detail=movie_detail,
                           movie_release_date=movie_release_date, movie_review=movie_review)
    movie_info.save()
    return render(request, "MovieReviewer/add_movie.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
