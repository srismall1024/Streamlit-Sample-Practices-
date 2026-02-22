import streamlit as st
import pandas as pd
import plotly.express as px

st.title("expense track expenser")
st.header("Know your path of expenses")

if "expenses" not in st.session_state:
    st.session_state.expenses=[]

if "sums" not in st.session_state:
    st.session_state.sums={
        "households":0,
        "bank":0,
        "office":0
        }

num=st.number_input("enter the number of entries for this month")
month=st.selectbox("choose the month",["Jan","Feb","Mar","Apr","May","June","Jul","Aug","Sep","Oct","Nov","Dec"])


for i in range(1,int(num)+1):
    ent=st.number_input("enter the amount",key=f"amount_{i}")
    cat=st.selectbox("select category",["households","bank","office"],key=f"category_{i}")
    submit=st.button("add to expenses",key=f"subs_{i}")
    if submit:

        st.session_state.expenses.append({
        "expended_amount":ent,
        "category":cat
        })

        st.session_state.sums[cat]+=ent

df=pd.DataFrame(st.session_state.expenses)
if not df.empty:
    fig=px.pie(df,names="category",values="expended_amount",title="expenditure track")
    st.plotly_chart(fig)
else:
    st.write("no responses added yet")
st.write("the expected data are below")
st.write("the households sums are",st.session_state.sums["households"])
st.write("the bank sums are",st.session_state.sums["bank"])
st.write("the office sums are",st.session_state.sums["office"])

    
