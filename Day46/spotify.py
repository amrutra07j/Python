import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which date do you want to travel to? Enter the date in format YYYY-MM-DD: ")
song_data = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(song_data.text, "html.parser")
songs = soup.find_all(class_="a-no-trucate", id="title-of-a-story")
songs_list = [song.getText().strip() for song in songs]


scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, show_dialog=True, cache_path='.cache'))
user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)