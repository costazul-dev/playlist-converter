# spotify_client.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

def get_spotify_client():
    """
    Initializes and returns a Spotipy client using a cache file for authentication.
    """
    scope = "playlist-read-private"
    
    # This creates a cache file to store your login information
    cache_handler = spotipy.CacheFileHandler(cache_path='./.spotify_cache')
    
    auth_manager = SpotifyOAuth(
        client_id=config.SPOTIPY_CLIENT_ID,
        client_secret=config.SPOTIPY_CLIENT_SECRET,
        redirect_uri=config.SPOTIPY_REDIRECT_URI,
        scope=scope,
        cache_handler=cache_handler,
        show_dialog=True  # Ensures the auth dialog appears every time if needed
    )
    
    return spotipy.Spotify(auth_manager=auth_manager)

def get_playlist_tracks(playlist_url):
    """
    Fetches all tracks from a given Spotify playlist URL.
    Returns a list of dictionaries, each with 'artist' and 'name'.
    """
    sp = get_spotify_client()
    playlist_id = playlist_url.split('/')[-1].split('?')[0]
    
    results = sp.playlist_items(playlist_id)
    tracks = results['items']
    
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
        
    track_list = []
    for item in tracks:
        if item['track']:
            track_name = item['track']['name']
            artist_name = item['track']['artists'][0]['name']
            track_list.append({'artist': artist_name, 'name': track_name})
            
    return track_list