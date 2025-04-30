# downloader/youtube_downloader.py

import yt_dlp
import os

def download_video(url, save_path="downloads"):
    os.makedirs(save_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        if filename.endswith(".webm"):
            filename = filename.replace(".webm", ".mp4")  # fallback if mp4 not available
        return filename
