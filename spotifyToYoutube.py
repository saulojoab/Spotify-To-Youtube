#coding: utf-8
import json
# Spotify library.
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# URL conversions.
import urllib.request
import bs4
# Youtube stuff.
import youtube

# Opening our JSON configuration file (which has our tokens).
with open("config.json", encoding='utf-8-sig') as json_file:
    APIs = json.load(json_file)

def getTracks(playlistURL):
    # Creating and authenticating our Spotify app.
    client_credentials_manager = SpotifyClientCredentials(APIs["spotify"]["client_id"], APIs["spotify"]["client_secret"])
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

def searchYoutubeAlternative(songName):
    # YouTube will block you if you query too many songs using this search.
    textToSearch = songName
    query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = bs4(html, 'html.parser')
    for vid in soup.findAll(attrs={'class': 'yt-uix-tile-link'}):
        print('https://www.youtube.com' + vid['href'])

def searchYoutube(songName):
    api = youtube.API(client_id=APIs["youtube"]["client_id"],
              client_secret=APIs["youtube"]["client_secret"],
              api_key=APIs["youtube"]["api_key"]);
    video = api.get('search', q=songName, maxResults=1, type='video', order='relevance');
    return("https://www.youtube.com/watch?v="+video["items"][0]["id"]["videoId"]);

if (__name__ == "__main__"):
    tracks = getTracks(str(input("Insert Spotify playlist URL: ")));
    print("Searching songs...");
    songs = [];
    for i in tracks:
        songs.append(searchYoutube(i));
    print("Search finished!");

    print("URL LIST: ");
    for i in songs:
        print(i);