from spotipy import Spotify, CacheFileHandler
from flask import request, session, url_for, redirect, render_template, flash
from .helpers import CACHE_FOLDER, create_spotify_oauth, get_recommended_tracks, create_playlist
from . import app
import os



# route for login page
@app.route('/', methods=('GET', 'POST'))
def login():
    pass


# route to handle Spotify API callback
@app.route('/callback/')
def callback():
    pass


# route for main page
@app.route('/home', methods=('GET', 'POST'))
def home():
    pass


# route for handling user logout
@app.route('/logout')
def logout():
    pass