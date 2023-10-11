function redirectToSpotify() {
    // AJAX request to logout route
    fetch('/logout', {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => response.json()) 
    .then(data => {
        if (data.success) { 

            // redirect to Spotify Logout page
            window.open('https://accounts.spotify.com/logout', '_blank');
        }

        // make another AJAX request and wait for response
        return fetch('/post_spotify_logout', {  
            method: 'GET',
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        });
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect_url) {

            // redirect to target URL
            window.location.href = data.redirect_url; 
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}