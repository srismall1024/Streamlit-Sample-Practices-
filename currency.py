import streamlit as st
from forex_python.converter import CurrencyRates

C=CurrencyRates()

st.title("Welcome to currency converter")
st.header("find you money value")

amount=st.number_input("enter the amount")

from_cur=st.radio("select the initial currency",["USD","INR","EUR","GBP"])
to_cur=st.radio("select the final currency",["USD","INR","EUR","GBP"])

if st.button("convert"):
    result=C.convert(from_cur,to_cur,amount)
    rate=C.get_rate(from_cur,to_cur)

    st.write(f"rate is : 1 {from_cur} = {rate}{to_cur}")
    st.write(f"expected amount is {result: .2f} {to_cur}")



