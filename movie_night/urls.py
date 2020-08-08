from django.urls import path
from . import views
from datetime import date
urlpatterns = [
    path('', views.calendar, name='movie_homepage'),
]