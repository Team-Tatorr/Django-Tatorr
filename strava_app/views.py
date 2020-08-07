from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .utils import *


#REFRESH TOKENS:
# https://www.strava.com/oauth/token?client_id=51477&client_secret=390ea0fb22bb58c5f7005590ae8f934d914f7f2f&code=3351d1efa14ed2bebe000fef6f08d12336038101&grant_type=refresh_token

# Create your views here.
def strava_index(request):
    #URL = "https://www.strava.com/api/v3/athlete"
    #URL = 'http://echo.jsontest.com/key/value/one/two'
    #headers = "Authorization: Bearer 2e476e08a21fdfeb3ca8b37913b732e1d31f167f"
    #r = requests.get(URL)
    #base_url = 'https://strava.com/api/v3'
    #ACTIVIES_URL = 'https://www.strava.com/api/v3/athlete/activities?access_token='
    #TOKEN = '3351d1efa14ed2bebe000fef6f08d12336038101'
    #r = requests.get(ACTIVIES_URL+TOKEN)
    #r = token_check()
    #oauth = 'https://www.strava.com/oauth/authorize?client_id=51477&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all'

    requests.get(url=oauth)

#def redirect_view(request):