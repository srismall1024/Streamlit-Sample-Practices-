import streamlit as st
from datetime import datetime
import time

st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #f7971e, #ffd200, #f9d423, #ff4e50);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass-card {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

h1 {
    text-align: center;
    color: #2d3436;
    text-shadow: 0 0 15px #f1c40f;
}

.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 12px;
    background: #2d3436;
    color: #f1c40f;
    font-weight: bold;
    box-shadow: 0 0 15px #f1c40f;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #f1c40f;
    color: black;
    box-shadow: 0 0 30px #f1c40f, 0 0 60px #f1c40f;
}

div[data-baseweb="select"] > div,
input {
    background-color: rgba(255,255,255,0.2) !important;
    color: black !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)



st.title("positive music selection")
st.header("choose the positivity!!")

alt=st.time_input("enter the wakeup time")
ch=st.selectbox("choose the music",["music1","music2"])
sub=st.button("select the required positivity")

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
        p="C:/Users/Success/pages/Enjaami Thandhaane Song _ Idli.mp3"
        st.audio(r"C:/Users/Success/pages/Enjaami Thandhaane Song _ Idli.mp3")

    if ch=="music2":
        p="C:/Users/Success/pages/LEO Ordinary Person-Downringtone.com.mp3"
        st.audio(r"C:/Users/Success/pages/LEO Ordinary Person-Downringtone.com.mp3")

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

time.sleep()
st.rerun()
