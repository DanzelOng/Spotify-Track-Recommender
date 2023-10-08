from random import randrange
from spotipy import SpotifyOAuth, Spotify, CacheFileHandler
from .config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE
import itertools
import time
import os



# create a folder to store Spotify user cache files
CACHE_FOLDER = os.path.join(os.getcwd(), "spotify_cache/")

# create cache folder if does not exist
if not os.path.exists(CACHE_FOLDER):
    os.makedirs(CACHE_FOLDER)


# create oauth object for spotify authentication process
def create_spotify_oauth(user_id=False):
    if user_id:
        return SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE,
                            cache_handler=CacheFileHandler(cache_path=os.path.join(CACHE_FOLDER, f".cache-{user_id}"))           )
    else:
        return SpotifyOAuth(client_id=CLIENT_ID,
                            client_secret=CLIENT_SECRET,
                            redirect_uri=REDIRECT_URI,
                            scope=SCOPE)


