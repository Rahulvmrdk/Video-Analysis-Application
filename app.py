# streamlit_app.py

import streamlit as st
from downloader.youtube_downloader import download_video
from preprocessing.audio_extractor import extract_audio
from preprocessing.speech_recognition import transcribe_audio
from analysis.keyword_detector import find_keywords
from clipping.video_clipper import clip_video

# Streamlit UI
st.set_page_config(page_title="Video Highlight Extractor", layout="centered")
st.title("🎬 Video Highlight Extractor")
st.markdown("Extract key moments like **Unboxing**, **Feature Demos**, and **Final Verdict** from YouTube videos.")

# Input URL
video_url = st.text_input("📺 Enter YouTube Video URL")

# Buffer time selection
buffer_time = st.slider("Select buffer time before/after key moment (in seconds):", 5, 60, 15)

# Submit button
if st.button("🔍 Analyze and Extract Highlights"):
    if not video_url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        with st.spinner("⏳ Downloading video..."):
            video_path = download_video(video_url)

        with st.spinner("🔊 Extracting audio..."):
            audio_path = extract_audio(video_path)

        with st.spinner("🧠 Transcribing speech..."):
            transcript = transcribe_audio(audio_path)

        with st.spinner("🗂️ Detecting key moments..."):
            events = find_keywords(transcript, ["unbox", "feature", "verdict"])

        with st.spinner("✂️ Clipping video segments..."):
            for event, time in events.items():
                output = f"{event}_clip.mp4"
                clip_video(video_path, time - buffer_time, time + buffer_time, output)
                st.success(f"{event.capitalize()} clip created!")

                with open(output, "rb") as f:
                    st.download_button(f"⬇️ Download {event} Clip", f, file_name=output)

st.markdown("---")

