#coding: utf-8
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

with open("config.json", encoding='utf-8-sig') as json_file:
    SpotifyAPI = json.load(json_file)

client_credentials_manager = SpotifyClientCredentials(SpotifyAPI["client_id"], SpotifyAPI["client_secret"])
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.user_playlist_tracks(user="",playlist_id="https://open.spotify.com/user/loudcodes_/playlist/4fIylfM1cQuMLr7tVQpSYn?si=909vsBwrSv6IH2o3n63SIQ")
trackList = [];
for i in results["tracks"]["items"]:
    print(i["track"]["name"] + " - " + i["track"]["album"]["artists"][0]["name"])
