from spotipy import Spotify, CacheFileHandler
from flask import request, session, url_for, redirect, render_template, flash
from .helpers import CACHE_FOLDER, create_spotify_oauth, get_recommended_tracks, create_playlist
from . import app
import os



# route for login page
@app.route('/', methods=('GET', 'POST'))
def login():

    if request.method == 'GET':

        # retrieve user ID from session
        if session.get("user_id"):
            user_id = session.get("user_id")

            # create SpotifyOAuth pbject for user
            oauth_obj = create_spotify_oauth(user_id)

            # get the user cache file
            cache_file = CacheFileHandler(cache_path=os.path.join(CACHE_FOLDER, f".cache-{user_id}"))

            # get access token from user if applicable
            token = cache_file.get_cached_token()

            if token:
                # refreshes token 
                if oauth_obj.is_token_expired(token):
                    oauth_obj.refresh_access_token(token['refresh_token'])
                
                flash(f"Welcome back {user_id}!", category="info")

                # user is authenticated and redirected to home page
                return redirect(url_for("home"))
            
            # redirect user to Spotify Auth Page
            else:
                return redirect(oauth_obj.get_authorize_url(state=user_id)) 
        
        # return login page if no user ID
        else:
            return render_template("base.html")
    
    # create OAuth object and redirect to Spotify Auth Page
    if request.method == 'POST':
        # get user ID from forms
        input_id = request.form.get("user_id").strip()
        oauth_obj = create_spotify_oauth()

        return redirect(oauth_obj.get_authorize_url(state=input_id))


# route to handle Spotify API callback
@app.route('/callback/')
def callback():
    # prevent direct access to the route
    if not request.args.get("code"):
        flash("Can't access this URL directly.", category="danger")
        return redirect('/')

    # retrieve the value from state parameter
    state = request.args.get("state")
    oauth_obj = create_spotify_oauth(state)
    token_info = oauth_obj.get_access_token(request.args.get('code'))
    spotify_API = Spotify(auth=token_info['access_token'], auth_manager=oauth_obj)

    # get Spotify User ID of current user
    user_id = spotify_API.current_user()['id']

    if user_id == state:
        # create cache file and write token information for current user
        cache_file = CacheFileHandler(cache_path=os.path.join(CACHE_FOLDER, f".cache-{state}"))
        cache_file.save_token_to_cache(token_info)

        # store user ID in session
        session['user_id'] = state
        flash(f"Logged in as {user_id}", category="info")
        return redirect(url_for('home'))
    
    else:
        os.remove(os.path.join(CACHE_FOLDER, f".cache-{state}"))
        flash(f"{state} does not exist", category="danger")
        return redirect(url_for('login'))


# route for main page
@app.route('/home', methods=('GET', 'POST'))
def home():
    pass


# route for handling user logout
@app.route('/logout')
def logout():
    pass