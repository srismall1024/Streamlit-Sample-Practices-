import streamlit as st

st.set_page_config(page_title="Login page")

st.title("Login page")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

user=st.text_input("enter username")
password=st.text_input("enter password",type="password")
submit=st.button("login")

if submit:
    if user=="admin" and password=="abcd":
        st.session_state.logged_in=True
        st.switch_page("pages/streamlit_practice2.py")
    else:
        st.error("invalid credentials")


