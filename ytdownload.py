# # // capture requirements to install
# # pip freeze > requirements.txt

import os
import random
import shutil
from pathlib import Path

import moviepy.editor as mp
# // install requirements from requirements.txt
# pip install -r requirements.txt
# import moviepy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pytube import YouTube
from push_to_github import deploy

# Download youtube video from link and save to temp folder
def download_youtube_video(link):
    # link = input("Enter link here: ")

    url = YouTube(link)
    title = url.title

    print("downloading...")

    video = url.streams.get_highest_resolution()

    os.mkdir("./temp/")
    video.download("./temp/")
    print("Downloaded! :)")
    # name of video in temp folder
    video_name = os.listdir("./temp/")[0]
    if(video_name == ".DS_Store"):
        video_name = os.listdir("./temp/")[1]
        if(video_name.split(".")[1] != "mp4"):
            video_name = os.listdir("./temp/")[2]
    deploy()
    return [video_name, title]

# # Resize video to 1080x1920


# def get_video_link_and_resize_to_short(video_name):

#     # get video from temp folder
#     myClip = mp.VideoFileClip("./temp/" + video_name)
#     new_video = myClip.resize((1080, 1920))
#     # new_video.show()
#     os.mkdir("./temp/converted/")
#     converted_video_name = str(random.randint(1, 999)) + "Short.mp4"
#     new_video.write_videofile("./temp/converted/" + converted_video_name)

#     return converted_video_name

# # Merge video and audio


# def merge_video_audio(video, audio_path):

#     # random audio from audio folder
#     audio = random.choice(os.listdir(audio_path))

#     video = mp.VideoFileClip(video)
#     audio = mp.AudioFileClip(audio)
#     final = video.set_audio(audio)
#     filename = title+str(random.randint(1, 999)) + "Audio_Short.mp4"
#     final.write_videofile("final.mp4")


# def download_audio(link):
#     # link = input("Enter link here: ")

#     url = YouTube(link)
#     title = url.title

#     print("downloading....")

#     video = url.streams.get_audio_only()

#     # os.mkdir("./downloaded_audios/")
#     video.download("./downloaded_audios/")
#     print("Downloaded! :)")
#     # name of video in temp folder
#     audio_name = os.listdir("./downloaded_audios/")[0]
#     if(audio_name == ".DS_Store"):
#         audio_name = os.listdir("./downloaded_audios/")[1]
#         if(audio_name.split(".")[1] != "mp4"):
#             audio_name = os.listdir("./downloaded_audios/")[2]
#     return [audio_name, title]

# # Create short videos from long videos


# def convert_video_to_short(video_name):


#     video_path = "./temp/converted/" + video_name

#     myClip = mp.VideoFileClip(video_path)

#     # get duration of video
#     duration = myClip.duration

#     # ask user for audio path to merge with video or use default
#     audio_path = input("Enter audio path or press enter to use default: ")

#     # Divide duration by random number between 40 and 60
#     # 40-60 seconds
#     seconds = 0
#     while(seconds < duration):

#         start = seconds
#         end = start + random.randint(50, 55)
#         if(end > duration):
#             end = duration
#         print(start, "start", end, "end")
#         print("--"*10, "seconds", seconds, "--"*10)
#         seconds += end
#         print("--"*10, "After seconds", seconds, "--"*10)
#         print(start, "start", end, "end")
#         print("--"*10, "seconds", seconds, "--"*10)
#         video = "./created-short-videos/" + title + \
#             str(random.randint(1, 999)) + "Short.mp4"
#         ffmpeg_extract_subclip(video_path, start, end,
#                                targetname=video)
#         if(audio_path == "y"):
#             audio_path = "./downloaded_audios/"
#             merge_video_audio(video, audio_path)
#     # os.rmdir('./temp')
#     shutil.rmtree('./temp')  # delete temp folder and all files in it


# youtube_link = input("Enter link here: ")

# # Ask user if they want to download audio or video
# audio_or_video = input("Enter a for audio or v for video: ")

# if(audio_or_video == "a"):
#     # download audio
#     [audio_name, title] = download_audio(youtube_link)
#     print(audio_name, "audio_name")
#     # convert audio to short
#     # convert_video_to_short(audio_name, "a")

# elif(audio_or_video == "v"):
#     # # download youtube video
#     [youtube_name, title] = download_youtube_video(youtube_link)
#     print(youtube_name, "youtube_name")

#     # resize video to 1080x1920
#     resize_video_path = get_video_link_and_resize_to_short(youtube_name)

#     # convert video to short
#     convert_video_to_short(resize_video_path)

# # [youtube_name, title] = download_youtube_video(youtube_link)
# # print(youtube_name, "youtube_name")

# # # resize video to 1080x1920
# # resize_video_path = get_video_link_and_resize_to_short(youtube_name)

# # # convert video to short
# # convert_video_to_short(resize_video_path)
