from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.homepage, name='tator_homepage'),
    path('movies', include('movie_night.urls')),
    path('strava_app', include('strava_app.urls')),
]