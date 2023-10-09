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


def get_recommended_tracks(spotify_API, count):
    recommended_tracks , top_genre = None, None

    # get the user's recent played tracks
    recent_tracks = spotify_API.current_user_recently_played(limit=count)['items']

    if not recent_tracks:
        return recommended_tracks, top_genre

    artist_ids = [track['track']['artists'][0]['id'] for track in recent_tracks]
    track_ids = [track['track']['id'] for track in recent_tracks]

    artists_info = spotify_API.artists(artist_ids)['artists']

    artist_genre = [artist['genres'] if artist['genres'] else ['pop'] for artist in artists_info]

    genres = list(itertools.chain.from_iterable(artist_genre))
    top_genre = max(genres, key=lambda x: genres.count(x))

    zipped_data = zip(artist_ids, track_ids, artist_genre)
    filtered_data = list(filter(lambda x: top_genre in x[2], zipped_data))

    seed_artists = [i[0] for i in filtered_data]
    seed_tracks= [i[1] for i in filtered_data]

    while len(seed_artists) + len(seed_tracks) > 4:
        if len(seed_artists) > len(seed_tracks):
            seed_artists.pop(randrange(len(seed_artists)))
        else:
            seed_tracks.pop(randrange(len(seed_tracks)))

    # get recommended tracks
    recommended_tracks = spotify_API.recommendations(
        seed_genre=top_genre, 
        seed_artists=seed_artists, 
        seed_tracks=seed_tracks, 
        min_popularity=65, 
        limit=50
    )
    return recommended_tracks, top_genre


def create_playlist(playlist_name, tracks, user_id):
    cache_file = CacheFileHandler(cache_path=os.path.join(CACHE_FOLDER, f".cache-{user_id}"))
    token = cache_file.get_cached_token()
    spotify_API = Spotify(auth=token['access_token'])

    # create playlist
    playlist = spotify_API.user_playlist_create(user=user_id, name=playlist_name)
    spotify_API.user_playlist_add_tracks(user_id, playlist['id'], tracks)
    return playlist['name']