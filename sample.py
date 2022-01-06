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
<div class="jumbotron text-center" style='background-color: #fff'>
  <h1 style="margin: auto; width: 100%;">This value exists in Dataframe</h1>
</div>
 ''', unsafe_allow_html=True);
           #st.write("This value exists in Dataframe")
        else :
            st.markdown('''
            <div style="height:150px;width: 2%; background-color: white; float:left;left: 1500px; border-radius: 2px;"">
            </div>
                    <div>
		     <div style="height:100px;width: 22%; background-color: white; float:center; left: 1700px; border-radius: 20px; border: 2px solid #d9d9d9; border-right: right;">
                        <div style="font-family: Arial, Helvetica, sans-serif;text-align: center; font-weight: bold; font-size: 30px; padding: 10px 0px 0px 2px;">This value does not exists in Dataframe </div>
            </div>
	</div>
 ''', unsafe_allow_html=True);

          #st.write("This value does not exists in Dataframe")
    
    
    
#CompanyName=st.text_input("Company")
#Brandname=st.text_input("Brand")
#ContactNumber=st.text_input("Number")


