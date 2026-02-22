import streamlit as st

st.title("quiz practice")
st.header("attend the quiz and gain the confidence")

if "submission" not in st.session_state:
    st.session_state.submission=False

if "score" not in st.session_state:
    st.session_state.score=0

with st.form("my_form"):
    q1=st.radio("capital of Tamil Nadu is?",["Chennai","Bangalore","Hyderabad"])
    q2=st.radio("Capital of India is?",["New Delhi","New York","Muscat"])
    q3=st.radio("What is 2+2?",["4","5","6"])

    submit=st.form_submit_button("Click here to finish the quiz")

    if submit:

        if q1=="Chennai":
            st.session_state.score+=1

        if q2=="New Delhi":
            st.session_state.score+=1

        if q3=="4":
            st.session_state.score+=1

            
        st.session_state.submission=True

if st.session_state.submission:
    st.write("congratulations u have scored",st.session_state.score)


    
