from moviepy.editor import VideoFileClip

def clip_video(video_path, start_time, end_time, output_path):
    with VideoFileClip(video_path) as video:
        start_time = max(0, start_time)
        end_time = min(video.duration, end_time)

        print(f"Clipping from {start_time:.2f} to {end_time:.2f}")
        
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(
            output_path,
            codec="libx264",
            audio_codec="aac",
            logger=None,
            threads=4,
            preset="fast"
        )
