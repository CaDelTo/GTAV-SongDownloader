from pytube import YouTube
import urllib.request, re, os
def downloadSong(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_name = yt.title + '.mp3'
        stream.download(output_path, filename=file_name)
        print(f"Downloaded {file_name}")
    except Exception as e:
        print("Failed to download the song.")
def searchSong(song):
    song = song.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={song}"
    vidIds = re.findall(r"watch\?v=(\S{11})", urllib.request.urlopen(url).read().decode())
    return f"https://www.youtube.com/watch?v={vidIds[0]}"
def downloadTXTPlaylist(playlist):
    try:
        with open(playlist, 'r') as f:
            if not os.path.exists(GtavUserMusicPath):
                os.makedirs(GtavUserMusicPath)
            for line in f:
                downloadSong(searchSong(line), GtavUserMusicPath)
    except Exception as e:
        print("Failed to find the txt file.")
def downloadPlaylist(playlist_url):
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
q1 = input("Do you want to download a song or a playlist? ([1]song/[2]playlist): ")
if q1 == "1":
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