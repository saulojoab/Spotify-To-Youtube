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
    # In case there's only one artist.
    if (i["track"]["artists"].__len__() == 1):
        trackList.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"])
    # In case there's more than one artist.
    else:
        nameString = "";
        for index, b in enumerate(i["track"]["artists"]):
            nameString += (b["name"]);
            if (i["track"]["artists"].__len__() - 1 != index):
                nameString += ", ";
        trackList.append(i["track"]["name"] + " - " + nameString);

for i in trackList:
    print(i);