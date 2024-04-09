import os
import streamlit as st
from pytube import YouTube


PATH_VIDEOS = os.path.join(os.path.dirname(__file__), 'videos')


if __name__ == '__main__':
    if not os.path.exists(PATH_VIDEOS):
        os.mkdir(PATH_VIDEOS)
        
    st.set_page_config(
        page_title="Youtube Download",
        page_icon=":fast_forward:",
        layout="centered"
    )
    
    st.title("YouTube Downloader")
    with st.container():
        youtube_url = st.text_input("Youtube URL")
        
        if youtube_url:
            yt = YouTube(youtube_url)
            st.image(yt.thumbnail_url)
            bt_download = st.button("Download video", use_container_width=True)
            
            if bt_download:
                with st.spinner("Downloading...."):
                    stream = yt.streams.filter(file_extension='mp4').desc().first().download(PATH_VIDEOS)
                st.success("Video Downloaded!!")