from app import app
import requests
import time
import os

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/testing')
def testing():
    return {'testKey': "MYtestVal"}


@app.route('/auth')
def authorize():
    # store token in sessions/cookie?
    # CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
    # CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
    # ENCODED_AUTH = os.environ.get('SPOTIFY_ENCODED')

    auth = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic {PUT_AUTH_HERE}'
    }
    body = {
       'grant_type':'client_credentials' 
    }

    res = requests.post(
        'https://accounts.spotify.com/api/token', headers=auth, data=body
    )
    # token = res.json(['access_token'])

    return "Auth is OK"
