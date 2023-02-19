import os
import sys
from pytube import Search
from pytube import YouTube
import moviepy.editor as mp
import glob


def download_videos(n, x):
    # Create a directory to store the videos
    if not os.path.exists("Videos"):
        os.mkdir("Videos")

    # Search for videos of the singer
    query = x + " music videos"
    s = Search(query)
    searchResults = {}
    i = 0
    for v in s.results:
        if i < n and v.length < 600:
            try:
                searchResults[v.title] = v.watch_url
                youtubeObject = YouTube(v.watch_url)
                youtubeObject = youtubeObject.streams.get_highest_resolution().download(
                    output_path='Videos', filename=f"video{i+1}.mp4")
                print(f"Downloaded video {i + 1}: {v.title}")
                i = i+1
            except:
                print("error occured")


def convertToAudio(duration, n):
    if not os.path.exists("Audios"):
        os.mkdir("Audios")

    for i in range(n):
        clip = mp.VideoFileClip(f"Videos/video{i+1}.mp4").subclip(0, duration)
        clip.audio.write_audiofile(f"Audios/audio{i+1}.mp3")


def makeMashup(n, output):
    audio_clips = [mp.AudioFileClip(
        f"Audios/audio{i+1}.mp3") for i in range(0, n)]
    final_clip = mp.concatenate_audioclips(audio_clips)
    final_clip.write_audiofile(output)


# download_videos(3, "Sidhu Moosewala")
# convertToAudio(20, 3)
# makeMashup(3)


if __name__ == "__main__":
    if (len(sys.argv) != 5):
        print("ERROR: Number of arguments are not correct")
        exit()

    download_videos(int(sys.argv[2]), sys.argv[1])
    convertToAudio(int(sys.argv[3]), int(sys.argv[2]))
    makeMashup(int(sys.argv[2]), sys.argv[4])
