import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
df
your_name = st.text_input("Number")
def search(your_name, df['phone']):
    for i in range(len(list)):
        if list[i] == your_name:
            return True
    return False
if search(df['phone'],your_name):
    print("Platform is found")
else:
    print("Platform does not found")
