import streamlit as st

st.title("Multiplication table generator")
st.header("Enter the number as your wish and generate the multiplication table")

n=st.number_input("enter the number you want to generate the table")
button=st.button("click here to generate")

if button:
    for i in range(1,11):
        st.write(n,"x",i,"=",n*i)

