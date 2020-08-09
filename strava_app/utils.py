# Imports #
import requests
import json
import os

AUTH_LINK = "https://www.strava.com/oauth/token"
ACCESS_TOKEN = ''
REFRESH_TOKEN = ''
EXPIRES_AT = 0
EXPIRES_IN = 0

#https://www.strava.com/oauth/authorize?client_id=51477&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all

def refresh_token(refresh_token=''):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }

    params = {
        'client_id': '51477',
        'client_secret': os.environ.get('STRAVA_CLIENT_SECRET'),
        'refresh_token': '84d2162a5e71cc19cc2b184f08844c8fee59cd66',
        'grant_type': 'refresh_token',
    }

    r = requests.post(url=AUTH_LINK, headers=headers, params=params)
    r.raise_for_status()
    return r.json()


token = refresh_token()
ACCESS_TOKEN = token['access_token']
REFRESH_TOKEN = token['refresh_token']
EXPIRES_AT = token['expires_at']
EXPIRES_IN = token['expires_in']

#TODO: Debugging using limited Activities
def getActivites():
    activities_link = "https://www.strava.com/api/v3/athlete/activities"
    header = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
    r = requests.get(url=activities_link, headers=header)
    return r.json()

def kudo_counter():
    x = getActivites()
    kudos_total = 0
    for run in x:
        kudos_total = kudos_total + run["kudos_count"]
    return kudos_total

print(kudo_counter())