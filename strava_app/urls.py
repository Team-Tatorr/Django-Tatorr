from django.urls import path
from . import views

urlpatterns = [
    # /strava_app/ index page
    path('', views.index, name='index'),
]