import streamlit as st
import pandas as pd
import numpy as np
#df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
#df

#your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")

df=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")
#print(df['Contact Number'])
your_name=st.text_input("Number")
res = df.isin([your_name]).any().any()

if res :
   print("\nThis value exists in Dataframe")

else :
   print("\nThis value does not exists in Dataframe")


