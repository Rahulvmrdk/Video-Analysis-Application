# clipping/video_clipper.py

#from moviepy import VideoFileClip
from moviepy.editor import VideoFileClip  # ✅ Correct import for MoviePy 2.x
# moviepy.video.io.VideoFileClip import VideoFileClip

def clip_video(video_path, start_time, end_time, output_path):
    with VideoFileClip(video_path) as video:  # Use context manager for cleanup
        start_time = max(0, start_time)
        end_time = min(video.duration, end_time)
        
        clip = video.subclip(start_time, end_time)  # ✅ Modern MoviePy uses `subclip()`
        
        clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            logger=None,  # Disables progress logs
            threads=4,   # Speeds up encoding
            preset="fast"  # Balances speed/quality
        )
