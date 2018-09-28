from django.db import models


class MovieInfo(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_review = models.CharField(max_length=3)
    movie_release_date = models.CharField(max_length=20)
    movie_type = models.CharField(max_length=50)
    movie_detail = models.TextField(max_length=500)

    def __str__(self):
        return self.movie_name


class MovieInfo_Test(models.Model):
    movie_test = models.CharField(max_length=100)

    def __str__(self):
        return self.movie_test
