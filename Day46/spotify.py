import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "d924c6afe3884bfcbca4d2724d4ab88a"

sp = spotipy.Spotify(scope)
print(sp)

date = input("Which date do you want to travel to? Enter the date in format YYYY-MM-DD: ")
song_data = requests.get("https://www.cricbuzz.com/", verify=False)
print(song_data.text)