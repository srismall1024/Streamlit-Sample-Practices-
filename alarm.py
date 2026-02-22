import streamlit as st
import datetime


st.set_page_config(page_title="mood based alarm")

st.markdown("""
<style>

/* ---------- Animated Background ---------- */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(-45deg, #141e30, #243b55, #0f2027, #2c5364);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ---------- Glass Card ---------- */
.glass-card {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(15px);
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    border: 1px solid rgba(255,255,255,0.2);
}

/* ---------- Titles ---------- */
h1 {
    text-align: center;
    font-size: 42px;
    color: #ffffff;
    text-shadow: 0 0 15px #00f7ff;
}

h2 {
    text-align: center;
    color: #dfe6e9;
}

/* ---------- Neon Buttons ---------- */
.stButton>button {
    width: 100%;
    height: 3em;
    border-radius: 12px;
    border: none;
    background: #111;
    color: #00f7ff;
    font-weight: bold;
    box-shadow: 0 0 12px #00f7ff;
    transition: 0.3s ease;
}

.stButton>button:hover {
    background: #00f7ff;
    color: black;
    box-shadow: 0 0 25px #00f7ff, 0 0 50px #00f7ff;
}

/* ---------- Inputs ---------- */
div[data-baseweb="select"] > div,
input {
    background-color: rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 10px !important;
}

</style>
""", unsafe_allow_html=True)


st.title("mood based alarm")
st.header("select the music to make your way")

tab1,tab2=st.tabs(["Tab1","Tab2"])
col1,col2,col3=st.columns(3)

with tab1:
    with col1:
        st.image(r"C:\\cs gate prep\\calm.jpg")
        b1=st.button("Calm and Composed alarm")
        if b1:
            st.switch_page("pages\\calm.py")
    with col2:
        st.image(r"C:\\cs gate prep\\energy.jpeg")
        b2=st.button("energetic alarm")
        if b2:
            st.switch_page("pages\\energetic.py")
    with col3:
        st.image(r"C:\\cs gate prep\\positive.jpg")
        b3=st.button("positive vibe alarm")
        if b3:
            st.switch_page("pages\\positivity.py")



