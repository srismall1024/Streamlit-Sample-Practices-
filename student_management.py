import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

conn=sqlite3.connect("bala.db",check_same_thread=False)
cursor=conn.cursor()

cursor.execute("""
create table if not exists student (
    id integer primary key autoincrement,
    regno text unique,
    Name text,
    Mathsmark integer,
    Physicsmark integer,
    Chemmark integer
    )
    """)
conn.commit()

st.title("student management system")

reg_no=st.text_input("enter the registration number:")
names=st.text_input("enter the student name:")
math=st.number_input("enter marks for maths:")
phy=st.number_input("enter marks for physics:")
chem=st.number_input("enter marks for chemistry:")

but=st.button("add Student")

if but:
    
    try:
        cursor.execute("insert into student(regno,Name,Mathsmark,Physicsmark,Chemmark) values (?,?,?,?,?)",(reg_no,names,math,phy,chem))
        conn.commit()
        st.success("data inserted successfully")

    except sqlite3.IntegrityError:
        st.error("regsitration number is already found")

but2=st.button("view student")

if but2:
    
    cursor.execute("select * from student")
    rows=cursor.fetchall()
    
    if rows:
        df=pd.DataFrame(rows,columns=["id","regno","Name","Mathsmark","Physicsmark","Chemmark"])
        st.dataframe(df)
        fig1=px.pie(df,names="Name",values="Mathsmark",title="mark conclusion-1")
        fig2=px.pie(df,names="Name",values="Physicsmark",title="mark conclusion-2")
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
    else:
        st.warning("No data found")



    
    

    
    
    
    

