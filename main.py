from pytube import YouTube
import urllib.request, re, os

def downloadSong(url, output_path):
    """
    Downloads a song from a given URL and saves it to the specified output path.

    Args:
        url (str): The URL of the song to download.
        output_path (str): The path where the downloaded song will be saved.

    Returns:
        None
    """
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_name = yt.title + '.mp3'
        stream.download(output_path, filename=file_name)
        print(f"Downloaded {file_name}")
    except Exception as e:
        print("Failed to download the song.")

def searchSong(song):
    """
    Searches for a song on YouTube and returns the URL of the first search result.

    Args:
        song (str): The name of the song to search for.

    Returns:
        str: The URL of the first search result on YouTube.
    """
    song = song.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={song}"
    vidIds = re.findall(r"watch\?v=(\S{11})", urllib.request.urlopen(url).read().decode())
    return f"https://www.youtube.com/watch?v={vidIds[0]}"

def downloadTXTPlaylist(playlist):
    """
    Downloads a playlist of songs from a text file.

    Args:
        playlist (str): The path to the text file containing the list of songs.

    Returns:
        None
    """
    try:
        with open(playlist, 'r') as f:
            for line in f:
                downloadSong(searchSong(line), GtavUserMusicPath)
    except Exception as e:
        print("Failed to find the txt file.")

def downloadPlaylist(playlist_url):
    """
    Downloads a playlist of songs from a YouTube playlist URL.

    Args:
        playlist_url (str): The URL of the YouTube playlist.

    Returns:
        None
    """
    try:
        playlist = YouTube(playlist_url)
        for video in playlist.videos:
            stream = video.streams.get_audio_only()
            file_name = video.title + '.mp3'
            stream.download(GtavUserMusicPath, filename=file_name)
            print(f"Downloaded {file_name}")
    except Exception as e:
        print("Failed to download the playlist.")

GtavUserMusicPath = os.path.expanduser("~/Documents/Rockstar Games/GTA V/User Music")
if not os.path.exists(GtavUserMusicPath):
    os.makedirs(GtavUserMusicPath)

q1 = input("Do you want to download a song or a playlist? ([1]song/[2]playlist): ")
if q1 == "1":
    q3 = input("Do you want to download the song from a URL or search for it? ([1]URL/[2]search): ")
    if q3 == "1":
        songURL = input("Enter the song URL: ")
        downloadSong(songURL, GtavUserMusicPath)
    elif q3 == "2":
        song = input("Enter the song name: ")
        downloadSong(searchSong(song), GtavUserMusicPath)
elif q1 == "2":
    q2 = input("Do you have the playlist URL from youtube or a list in a txt file? ([1]URL/[2]file): ")
    if q2 == "1":
        playlistURL = input("Enter the playlist URL: ")
        downloadPlaylist(playlistURL)
    elif q2 == "2":
        playlistTXT = input("Enter the playlist file name (txt file): ")
        if not playlistTXT.endswith(".txt"):
            playlistTXT = playlistTXT + ".txt"
        downloadTXTPlaylist(playlistTXT)
