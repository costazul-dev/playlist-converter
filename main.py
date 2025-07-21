# main.py
import os
from spotify_client import get_playlist_tracks, get_spotify_client
from youtube_client import search_for_video

def get_playlist_name(playlist_url):
    """
    Gets the name of a Spotify playlist from its URL.
    """
    try:
        sp = get_spotify_client()
        playlist_id = playlist_url.split('/')[-1].split('?')[0]
        playlist = sp.playlist(playlist_id)
        return playlist['name']
    except Exception as e:
        print(f"Error getting playlist name: {e}")
        return "Unknown_Playlist"

def sanitize_filename(filename):
    """
    Removes or replaces characters that aren't allowed in filenames.
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename.strip()

def convert_playlist(playlist_url):
    """
    Converts a Spotify playlist to YouTube links and saves to a file.
    Returns a summary of the conversion.
    """
    # Get playlist name
    playlist_name = get_playlist_name(playlist_url)
    safe_playlist_name = sanitize_filename(playlist_name)
    
    # Create playlists directory if it doesn't exist
    if not os.path.exists('playlists'):
        os.makedirs('playlists')
    
    # Get tracks from Spotify
    spotify_tracks = get_playlist_tracks(playlist_url)
    
    if not spotify_tracks:
        return f"Could not fetch tracks from playlist: {playlist_name}"
    
    # Search for YouTube links
    youtube_links = []
    successful_conversions = 0
    
    for track in spotify_tracks:
        query = f"{track['artist']} - {track['name']}"
        youtube_link = search_for_video(query)
        if youtube_link:
            youtube_links.append(f"{track['artist']} - {track['name']}: {youtube_link}")
            successful_conversions += 1
        else:
            youtube_links.append(f"{track['artist']} - {track['name']}: NOT FOUND")
    
    # Save to file
    filename = os.path.join('playlists', f"{safe_playlist_name}.txt")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"Playlist: {playlist_name}\n")
        f.write(f"Total tracks: {len(spotify_tracks)}\n")
        f.write(f"Successfully converted: {successful_conversions}\n")
        f.write("-" * 50 + "\n\n")
        for link in youtube_links:
            f.write(link + "\n")
    
    return f"Playlist '{playlist_name}' converted: {successful_conversions}/{len(spotify_tracks)} tracks found. Saved to {filename}"

if __name__ == '__main__':
    while True:
        # Ask for playlist URL
        playlist_url = input("Enter the Spotify playlist URL: ").strip()
        
        if not playlist_url:
            print("No URL provided. Exiting...")
            break
        
        # Convert the playlist
        summary = convert_playlist(playlist_url)
        print(summary)
        
        # Ask if user wants to convert another playlist
        while True:
            continue_choice = input("\nDo you want to convert another playlist? (y/n): ").strip().lower()
            if continue_choice in ['y', 'yes']:
                break
            elif continue_choice in ['n', 'no']:
                print("Done!")
                exit()
            else:
                print("Please enter 'y' for yes or 'n' for no.")