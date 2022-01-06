import streamlit as st
import pandas as pd
import numpy as np
#df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
#df

#your_name = st.text_input("Number")
#if your_name:
#  df[df['phone'] == your_name]
    #st.write("There is some value. Processing...")
    
 
    

st.markdown(
    """
<style>
  .reportview-container{
  background-image: url('https://images.unsplash.com/photo-1542281286-9e0a16bb7366');
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;}
  </style>
  """,
 unsafe_allow_html=True
)    


df=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vSjdA5Ku8OzMsGEStlOKciPERkgSLoCYxPObTbFbblm85P0xDtZM5C7fHsrgpEL0pdQCsrz-F_G-Rz3/pub?gid=1840897213&single=true&output=csv")


st.markdown('''
    <div>
    <h4 style="color:#33D1FF" "font-size:200%" align="center" >Enter Phone Number</h4>
    </div>
  ''', unsafe_allow_html=True);
if __name__ == '__main__':
    input = st.empty()    
    txt = input.text_input(" ")
    
    st.markdown('''
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    align="center";
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #00ff00;
    color:#ff0000;
    }
</style>
''', unsafe_allow_html=True)
col1, col2, col3 = st.beta_columns(3)

# this will put a button in the middle column
with col2:
    st.button("I am a button")
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


