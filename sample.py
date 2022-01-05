import streamlit as st
import pandas as pd
import numpy as np
df=pd.read_csv('Untitled spreadsheet - Sheet1.csv')
df
your_name = st.text_input("Number")
a=df[df['phone'] == 123]
a
