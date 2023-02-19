# Mashup

A python program that creates mashup of videos of your favourite singer.

## Tasks:

1. Search youtube for n number of videos of a singer
2. Download the video files.
3. Convert them to audio
4. Trim the audio files to certain duration
5. Merge all audio files

## Libraries Used:

1. pytube: to download video files from youtube
2. moviepy:	to convert video files to audio (mp3) files, trim and merge them

## Usage:

To run from cli, use the following command:

`` python 102003293.py [SingerName] [NumberOfVideos] [AudioDuration] [OutputFileName] ``


Example:

`` python 102003293.py Sidhu Moosewala 2 20 sidhu.mp3
