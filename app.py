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
energy_select=st.sidebar.selectbox('Select a state',df1['EnergySourceType'].unique())
selected_state = df[df['State']==state_select]
energy=df1[df1['EnergySourceType']==energy_select]
st.markdown('''
<div class="jumbotron text-center" style='background-color: #fff'>
  <h1 style="margin: auto; width: 100%;">Renewable Energy Dashboard</h1>
  <h2></h2>
  
</div>
''', unsafe_allow_html=True);
a=px.bar(selected_state,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
st.plotly_chart(a)

b=px.bar(energy,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
st.plotly_chart(b)
