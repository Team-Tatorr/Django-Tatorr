from django.urls import path
from . import views

urlpatterns = [
    # /strava_app/ index page
    path('', views.records, name='strava_records'),
    path('strava_login', views.strava_login, name='strava_login'),
]