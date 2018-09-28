from django.contrib import admin

from .models import MovieInfo
from .models import MovieInfo_Test

admin.site.register(MovieInfo)
admin.site.register(MovieInfo_Test)