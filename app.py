import streamlit as st
import pandas as pd
import numpy as np 
from PIL import Image
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
df=pd.read_csv('A.csv')
df1=pd.read_csv('B.csv')
df2=pd.read_csv('C.csv')
st.sidebar.title("Menu")
state_select = st.sidebar.selectbox('Select a state',df['State'].unique())
selected_state = df[df['State']==state_select]
a=px.bar(selected_state,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
st.plotly_chart(a)
