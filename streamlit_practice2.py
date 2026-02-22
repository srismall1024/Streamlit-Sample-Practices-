import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Sample page 2")
st.header("Just fill the content in the pages")
tab1,tab2,tab3=st.tabs(["Tab1","Tab2","Tab3"])

with st.form("my_form"):
    with tab1:
        name=st.text_input("enter your name")
        dob=st.date_input("enter date of birth")
        age=st.number_input("enter age")
    with tab2:
        math=st.number_input("enter marks for maths(out of 100)")
        phy=st.number_input("enter marks for physics(out of 100)")
        chem=st.number_input("enter marks for chemistry(out of 100)")
        comp=st.number_input("enter marks for computer science(out of 100)")
        eng=st.number_input("enter marks for english(out of 100)")
    submit=st.form_submit_button("submit")

if submit:
    with tab3:
        st.write("the total marks is",math+phy+chem+comp+eng)
        data={
            "subject":["Maths","Physics","chemistry","computer science","english"],
            "mark":[math,phy,chem,comp,eng]
            }
        df=pd.DataFrame(data)
        col1,col2,col3=st.columns(3)
        with col1:
            fig=px.pie(df,names="subject",values="mark",title="subject-marks distribution")
            st.plotly_chart(fig)
        with col2:
            st.bar_chart(df.set_index("subject"))
        with col3:
            st.area_chart(df.set_index("subject"))

    
    
