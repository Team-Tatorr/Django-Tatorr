from django.shortcuts import render
from django.http import HttpResponse
from strava_app.utils import *
# Create your views here.
def records(request):

    return render(request, "strava_app/index.html", {'kudo_count': kudo_counter()})

def strava_login(request):
    return render(request, "strava_app/index.html", {'kudo_count': "tacos"})
