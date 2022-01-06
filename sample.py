import streamlit as st
import pandas as pd
import numpy as np
#df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
#df

#your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")
    
st.markdown('''
page_bg_img =
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
''',unsafe_allow_html=True)
   
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
    }
   .sidebar .sidebar-content {
        background: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366")
    }
    </style>
    """,
    unsafe_allow_html=True
)    

    
df=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")

if __name__ == '__main__':
    input = st.empty()
    txt = input.text_input("Insert number:")
    bt = st.button("Search")

    if bt:
        #txt = "txt"
        #input.text_input("Insert Number:", value=txt)
        res = df.isin([txt]).any().any()
        if res :
            st.markdown('''
<div>
  <h3 style="color:red" "font-size:200%" align="center" >This value exists in Dataframe</h3>
</div>
 ''', unsafe_allow_html=True);
           #st.write("This value exists in Dataframe")
        else :
            st.markdown('''
<div>
  <h3 style="color:green" "font-size:200%" align="center" >This value does not exists in Dataframe</h3>
</div>
 ''', unsafe_allow_html=True);

          #st.write("This value does not exists in Dataframe")
    
    
    
#CompanyName=st.text_input("Company")
#Brandname=st.text_input("Brand")
#ContactNumber=st.text_input("Number")


