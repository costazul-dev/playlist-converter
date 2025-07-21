# Spotify to YouTube Playlist Converter

Convert your Spotify playlists to YouTube links - find the corresponding YouTube videos for all songs in your Spotify playlists.

## Features

- Convert Spotify playlist URLs to YouTube video links
- Automatic playlist name detection and file organization
- High success rate for finding matching videos
- Clean text file output with playlist information

## Prerequisites

- Python 3.6+

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/costazul-dev/playlist-converter.git
cd playlist-converter
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Get API credentials

#### Spotify API:
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy your Client ID and Client Secret
4. Set redirect URI to `https://www.google.com`

#### YouTube Data API:
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable YouTube Data API v3
4. Create credentials (API key)
5. Copy your API key

### 4. Configure environment variables
```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual credentials
nano .env  # or your preferred editor
```

## Usage

### Convert Spotify playlists to YouTube links
```bash
python main.py
```
Enter your Spotify playlist URL when prompted. The script will create a text file in the `playlists/` directory with YouTube links for each song.

## File Structure

```
playlist-converter/
├── main.py                 # Main conversion script
├── spotify_client.py       # Spotify API wrapper
├── youtube_client.py       # YouTube API wrapper
├── config.py              # Configuration management
├── playlists/             # Generated playlist files
├── .env                   # Your API credentials (not in repo)
├── .env.example           # Template for credentials
└── requirements.txt       # Python dependencies
```

## Output Format

The generated text files contain:
- Playlist name and metadata
- List of songs with their corresponding YouTube links
- Conversion success statistics

Example output:
```
Playlist: My Awesome Playlist
Total tracks: 25
Successfully converted: 23
--------------------------------------------------

Artist Name - Song Title: https://www.youtube.com/watch?v=VIDEO_ID
Another Artist - Another Song: https://www.youtube.com/watch?v=VIDEO_ID
...
```

## Notes

- The first time you run the script, you'll need to authenticate with Spotify through your browser
- YouTube searches return the top result for each track - results may vary in accuracy
- The `.spotify_cache` file stores your authentication token for future use
- Generated playlist files are saved in the `playlists/` directory

## Troubleshooting

### "Missing required environment variables"
Make sure you've created the `.env` file and filled in all required credentials.

### "Command not found" or import errors
Make sure you've installed all dependencies: `pip install -r requirements.txt`

### Low conversion success rate
This can happen if song titles or artist names don't match exactly between Spotify and YouTube. The script uses the top search result for each query.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.