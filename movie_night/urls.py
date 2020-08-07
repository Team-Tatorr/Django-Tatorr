from django.urls import path
from . import views
urlpatterns = [
    path('', views.movie_calendar, name='movie_homepage'),
]