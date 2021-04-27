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
#st.sidebar.title("Menu")
state_select = st.selectbox('Select a state',df['State'].unique())
energy_select=st.selectbox('Select a Energy Type',df1['EnergySourceType'].unique())
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
st.markdown("## **Energy Generation By Source**")
b=px.bar(energy,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
st.plotly_chart(b)
st.markdown("## **Energy Generation By Source**")
state_select1 = st.selectbox('Select a state',df2['State'].unique())
selected_state1 = df2[df2['State']==state_select1]
c=px.bar(selected_state1,x='YearValue',y='Generation_GWh')
st.plotly_chart(c)
