# preprocessing/audio_extractor.py

from moviepy import VideoFileClip
import os

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path, logger=None)
    return audio_path
