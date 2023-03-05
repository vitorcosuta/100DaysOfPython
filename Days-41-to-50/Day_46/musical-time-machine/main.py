import requests
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

# Webscraping
date_in_time = input('Which year do you want to? Type the date in this format YYYY-MM-DD: ')

billboard_url = f'https://www.billboard.com/charts/hot-100/{date_in_time}/'
response = requests.get(billboard_url)
response.raise_for_status()
billboard_web_page = response.text

soup = BeautifulSoup(billboard_web_page, 'html.parser')

top_100_songs = [song.getText() for song in soup.select('li ul li h3')]

top_100_songs = [song.replace('\n', '') for song in top_100_songs]
top_100_songs = [song.replace('\t', '') for song in top_100_songs]

print(top_100_songs)

# Spotify Authentication
auth_manager = SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                            client_secret=SPOTIFY_CLIENT_SECRET,
                            redirect_uri='http://localhost:8888/callback',
                            scope='playlist-modify-private',
                            show_dialog=True,
                            cache_path='token.txt')

sp = spotipy.Spotify(auth_manager=auth_manager)

# Splitting the date that was previously collected
song_year = date_in_time.split('-')[0]
song_month = date_in_time.split('-')[1]
song_day = date_in_time.split('-')[2]

spotify_songs_URI = []

# Searching for each song's Spotify URI
for song in top_100_songs:
    query = f'track:{song} year:{song_year}'
    search = sp.search(q=query, type='track', limit=1)

    try:
        song_URI = search['tracks']['items'][0]['uri']
        spotify_songs_URI.append(song_URI)
    except IndexError:
        print(f'{song} is not available in Spotify. Skipped.')


print(spotify_songs_URI)

# Obtaining the current user's id
user_id = sp.current_user()['id']

# Creating a private playlist for the current user
playlist = sp.user_playlist_create(user=user_id,
                                   name=f'{date_in_time} Billboard 100',
                                   public=False,
                                   collaborative=False,
                                   description=f"Songs that reached the Top 100 Billboard in "
                                               f"{song_day}/{song_month}/{song_year}.")

playlist_id = playlist['id']
sp.playlist_add_items(playlist_id=playlist_id, items=spotify_songs_URI)
