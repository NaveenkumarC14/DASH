import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
df

your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")

mytext = st.text_input('enter text')
st.write(pd.DataFrame({'df' : [mytext,mytext,mytext]}))


