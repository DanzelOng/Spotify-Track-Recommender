# Spotify Track Recommendation App using Python
This application provides personalized track recommendations by analyzing users' recently played tracks on Spotify. 
It identifies the most frequented music genre and generates a playlist based on the top genre.

## Technologies Used
* Backend: Python with Flask Framework
* Frontend: Javascript, HTML with CSS and Bootstrap 5
* API Integration: Spotipy
* Templating: Jinja

## Features
### User login
User login utilizes the Spotify's Authorization Code Flow, which ensures that first-time users grant app permissions only once.
The access token is checked for subsequent login attempts and refreshed for expired tokens in order to re-authenticate the user to the app.

### Main Page
* Users can choose the number of recently played tracks for genre analysis and playlist genration.

### Playlist Generation
* Generates a custom playlist based on the user's top genre.

### Save Playlist
* Users can choose to name and save the playlist directly to their Spotify account.

## User logout
Users are directed to the Spotify Logout Page during the logout process, which term
The app also initiates a separate process that redirects the home page back to the login page.
