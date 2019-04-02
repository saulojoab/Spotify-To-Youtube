# Spotify To Youtube ▶
A simplistic way to find Spotify songs on YouTube.

# How does it work? 😮
All you gotta do is insert your <b> >>PUBLIC<< </b> <a href="http://www.spotify.com">Spotify</a> playlist URL when prompted, then the app will automatically search all songs from that playlist on <a href="http://youtube.com">Youtube</a> and return the URLs. Check below for instructions on how to make it work:

# What did you use to make it? :thinking:
I used the following libraries:<br>
  - <a href="https://github.com/plamere/spotipy">Spotipy (For handling the Spotify API)</a>
  - <a href="https://github.com/rohitkhatri/youtube-python">YouTube Python (For handling the Youtube API)</a><br><br>
1 - To use those APIs, you gotta register your app on both the Spotify and YouTube API services.<br>
2 - When you finish doing that, <b>create a JSON file</b> named <i>"config.json"</i> on the project's main folder.<br>
3 - The <i>config.json</i> file <b>must have</b> the following format:
```js
{
    "spotify":
    {
        "client_id": "your_spotify_client_id",
        "client_secret": "your_spotify_client_secret"
    },
    "youtube":
    {
        "api_key": "your_youtube_api_key",
        "client_id": "your_youtube_client_id",
        "client_secret": "your_youtube_client_secret"
    }
}
```

# Why did you make it?
Studying purpouses, and it might actually be useful to someone. I think <a href="http://discord.app">Discord</a> bots could use that to queue songs and stuff. 
