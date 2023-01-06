import streamlit as st
from pytube import YouTube
import base64
from io import BytesIO

@st.cache()
def main():
    path= st.text_input("Enter Video URL: ")
    options = st.selectbox("Select the type of download",("Audio","High res Video","Low res Video"))

    if st.button("Download"):
        video_obj=YouTube(path)
        st.write("Video Title: "+ str(video_obj.title))
        st.write("Number of views: "+ str(video_obj.views))
        if (options=="Audio"):
            video_obj.streams.get_audio_only().download()
        elif (options=="High res Video"):
            video_obj.streams.get_highest_resolution().download()
        elif (options=="Low res Video"):
            video_obj.streams.get_lowest_resolution().download()


    if st.button("View"):
        st.video(path)




if __name__ == '__main__':
    main()