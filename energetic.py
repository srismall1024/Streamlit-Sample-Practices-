import streamlit as st
from datetime import datetime
import time

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #ff0000, #ff512f, #dd2476, #240b36);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass-card {
    background: rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.6);
}

h1 {
    text-align: center;
    color: #ffffff;
    text-shadow: 0 0 20px #ff004c;
}

.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 12px;
    background: black;
    color: #ff004c;
    font-weight: bold;
    box-shadow: 0 0 15px #ff004c;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #ff004c;
    color: white;
    box-shadow: 0 0 30px #ff004c, 0 0 60px #ff004c;
}

div[data-baseweb="select"] > div,
input {
    background-color: rgba(255,255,255,0.15) !important;
    color: white !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)


st.title("energetic music selection")
st.header("choose the energy!!")

alt=st.time_input("enter the wakeup time")
ch=st.selectbox("choose the music",["music1","music2"])
sub=st.button("select the energy consumption required")

if "selected" not in st.session_state:
    st.session_state.selected=False

if "alarm_set" not in st.session_state:
    st.session_state.alarm_set=None

if "alarm_status" not in st.session_state:
    st.session_state.alarm_status=False

if "music_sel" not in st.session_state:
    st.session_state.music_sel=None

if sub:
    
    if ch=="music1":
        p="C:/Users/Success/pages/LEO Ordinary Person-Downringtone.com.mp3"
        st.audio(r"C:/Users/Success/pages/LEO Ordinary Person-Downringtone.com.mp3")

    if ch=="music2":
        p="C:/Users/Success/pages/Devara - Red Sea BGM-Downringtone.com.mp3"
        st.audio(r"C:/Users/Success/pages/Devara - Red Sea BGM-Downringtone.com.mp3")

    st.session_state.selected=True
    st.session_state.alarm_status=True
    st.session_state.alarm_set=alt
    st.session_state.music_sel=p

    st.write("Alarm selected successfully")


if st.session_state.alarm_status:

    current_time=datetime.now().time()

    if (current_time.hour == st.session_state.alarm_set.hour and
        current_time.minute == st.session_state.alarm_set.minute):

        st.audio(st.session_state.music_sel,autoplay=True)

time.sleep(1)
st.rerun()
