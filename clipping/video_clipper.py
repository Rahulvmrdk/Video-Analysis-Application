# clipping/video_clipper.py

from moviepy import VideoFileClip

def clip_video(video_path, start_time, end_time, output_path):
    video = VideoFileClip(video_path)
    duration = video.duration
    start_time = max(0, start_time)
    end_time = min(duration, end_time)
    clip = video.subclip(start_time, end_time)
    clip.write_videofile(output_path, codec="libx264", audio_codec="aac", logger=None)
