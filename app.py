import os
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"

import streamlit as st
import whisper
import uuid

from downloader.youtube_downloader import download_video
from preprocessing.audio_extractor import extract_audio
from preprocessing.speech_recognition import transcribe_audio
from analysis.keyword_detector import find_keywords
from clipping.video_clipper import clip_video
from analysis.keyword_dete import find_keywords_with_timestamps

@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

st.set_page_config(page_title="Video Highlight Extractor", layout="centered")
st.title("🎬 Video Highlight Extractor")
st.markdown("Extract key moments like **Unboxing**, **Feature Demos**, and **Final Verdict** from YouTube videos.")

video_url = st.text_input("📺 Enter YouTube Video URL")
buffer_time = st.slider("Select buffer time before/after key moment (in seconds):", 5, 60, 15)

if st.button("🔍 Analyze and Extract Highlights"):
    if not video_url:
        st.warning("Please enter a valid YouTube URL.")
    else:
        with st.spinner("⏳ Downloading video..."):
            video_path = download_video(video_url)

        with st.spinner("🔊 Extracting audio..."):
            audio_path = extract_audio(video_path)

        with st.spinner("🧠 Transcribing speech..."):
            model = load_whisper_model()
            result = model.transcribe(audio_path)
            transcript = result['text']

        with st.spinner("🗂️ Detecting key moments..."):
            #events = find_keywords(transcript, ["unbox", "feature", "verdict"])
            events = find_keywords_with_timestamps(audio_path, ["unbox", "feature", "verdict"])
            
            if events:
                st.subheader("📍 Detected Key Moments:")
                for event, time in events.items():
                    st.markdown(f"**{event.capitalize()}** at **{time:.2f} seconds**")

        if not events:
            st.warning("No key moments found. Try a different video or keyword.")
        else:
            with st.spinner("✂️ Clipping video segments..."):
                for event, time in events.items():
                    output = f"{event}_{uuid.uuid4().hex[:6]}.mp4"
                    #-----------------------------------------------------------------
                    #clip_video(video_path, time - buffer_time, time + buffer_time, output)
                    #st.success(f"{event.capitalize()} clip created!")
                    #with open(output, "rb") as f:
                    #    st.download_button(f"⬇️ Download {event} Clip", f, file_name=output)
                    #-----------------------------------------------------------------
                    try:
                        clip_video(video_path, time - buffer_time, time + buffer_time, output)
                        st.success(f"{event.capitalize()} clip created!")
                        with open(output, "rb") as f:
                            st.download_button(f"⬇️ Download {event} Clip", f, file_name=output)
                    except Exception as e:
                        st.error(f"❌ Failed to create clip for {event}: {str(e)}")

st.markdown("---")
