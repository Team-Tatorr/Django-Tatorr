from django.urls import path
from . import views

urlpatterns = [
    # /strava_app/ index page
    path('', views.records, name='strava_records'),
    path('/auth/', views.records, name='tacos'),

    #path('/auth', views.strava_auth, name='strava_auth'),
]