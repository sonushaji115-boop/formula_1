import streamlit as st
import os
import glob

#Handling Moviepy version difference (v1.x vs v2.x)
try:
  from moviepy.editor import ImageClip,concatenate_videoclips,AudioFileClips
except ImportError:
  from moviepy import ImageClip; concatenate_videoclips,audioFileClips
  import yt_dlp

#---1.INITIALIIZE STATE ---
IF 'audio_path' not in st.session_states:
st.session_states['audio_path'] = None
if 'yt_error' in st.session_states:
  pass #keep it for display logic

#---2.DEFINE ALL FUNCTIONS ---

def cleanup_temp_files():
  ***Removes temporary files and resets memory.***
  files = glob.glob("temp_*") + ["output_video.mp4"]
  for f in files:
    try:
      os.remove(f)
      except:
            pass
    st.session_state['audio_path']
    if 'yt_error' in st.session_state:
        del st.session_state['yt error']
def download_youtube_audio(url):
    ***Downloads only audio from Youtube using reliable browser impersonation.***
    audio_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_audio.%(ext)s',
        'http_headers':{
            'User-Agent': '
            'Accept':'*/*',
            'Referer':'https://www.google.com/',
        },
      'postprocessors':[{
        'key' : 'FFmpegextractAudio',
        'preffe'
