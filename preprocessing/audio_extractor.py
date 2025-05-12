# preprocessing/audio_extractor.py

#from moviepy import 
from moviepy.editor import VideoFileClip  # ✅ Correct import for MoviePy 2.x
import os

def extract_audio(video_path):
    video = VideoFileClip(video_path)
    audio_path = video_path.replace(".mp4", ".wav")
    video.audio.write_audiofile(audio_path, logger=None)
    return audio_path
