#coding: utf-8
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def getTracks(playlistURL):
    # Opening our JSON configuration file (which has our tokens).
    with open("config.json", encoding='utf-8-sig') as json_file:
        SpotifyAPI = json.load(json_file)

    # Creating and authenticating our Spotify app.
    client_credentials_manager = SpotifyClientCredentials(SpotifyAPI["client_id"], SpotifyAPI["client_secret"])
    spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Getting a playlist.
    results = spotify.user_playlist_tracks(user="",playlist_id=playlistURL)

    trackList = [];
    # For each track in the playlist.
    for i in results["tracks"]["items"]:
        # In case there's only one artist.
        if (i["track"]["artists"].__len__() == 1):
            # We add trackName - artist.
            trackList.append(i["track"]["name"] + " - " + i["track"]["artists"][0]["name"])
        # In case there's more than one artist.
        else:
            nameString = "";
            # For each artist in the track.
            for index, b in enumerate(i["track"]["artists"]):
                nameString += (b["name"]);
                # If it isn't the last artist.
                if (i["track"]["artists"].__len__() - 1 != index):
                    nameString += ", ";
            # Adding the track to the list.
            trackList.append(i["track"]["name"] + " - " + nameString);

    return trackList;

if (__name__ == "__main__"):
    for i in getTracks("https://open.spotify.com/user/loudcodes_/playlist/4fIylfM1cQuMLr7tVQpSYn?si=xTELx4wkR_29J0n89I6dAQ"):
        print(i);