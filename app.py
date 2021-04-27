import streamlit as st
import pandas as pd
import numpy as np 
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
df=pd.read_csv('A.csv')
df1=pd.read_csv('B.csv')
df2=pd.read_csv('C.csv')
df3=pd.read_csv('Renewable Electricity Capacity by State_D_20210426_203204.csv')
df4=pd.read_csv('Electricity Potential by Energy Source_D_20210427_132109.csv')
df5=pd.read_csv('Renewable Electricity Capacity by State_D_20210426_203204.csv')
df6=pd.read_csv('Electricity Capacity by State_D_20210427_143749.csv')
df7=pd.read_csv('Electricity Capacity by Energy Source_D_20210427_143811.csv')
st.sidebar.title("Menu")
visualization = st.sidebar.selectbox('Select a type',('Potential','Generation','Capacity'))
if visualization=='Generation':
  
  st.markdown('''
    <div class="jumbotron text-center" style='background-color: #fff'>
    <h1 style="margin: auto; width: 100%;">Renewable Energy Dashboard</h1>
 
 
    </div>
    ''', unsafe_allow_html=True);
  state_select = st.selectbox('Select a state',df['State'].unique())

  selected_state = df[df['State']==state_select]
  a=px.bar(selected_state,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
  st.plotly_chart(a)

  st.markdown("## **Energy Generation By Source**")
  energy_select=st.radio('Select a Energy Type',df1['EnergySourceType'].unique())
  energy=df1[df1['EnergySourceType']==energy_select]
  b=px.bar(energy,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
  st.plotly_chart(b)
  st.markdown("## **Energy Generation By State**")
  state = st.selectbox('Select state',df2['State'].unique())
  selected = df2[df2['State']==state]
  c=px.bar(selected,x='YearValue',y='Generation_GWh')
  st.plotly_chart(c)
elif visualization=='Capacity':
  st.markdown("## **Energy Potential By State**")
  state_select = st.selectbox('Select a state',df6['State'].unique())
  selected_state = df6[df6['State']==state_select]
  a=px.bar(selected_state,x='YearValue',y='Capacity_MW')
  st.plotly_chart(a)
  st.markdown("## **Energy Generation By Source**")
  energy_select=st.radio('Select a Energy Type',df7['EnergySourceType'].unique())
  energy=df7[df7['EnergySourceType']==energy_select]
  b=px.bar(energy,x='YearValue',y='Capacity_MW',color='EnergySource',barmode='group')
  st.plotly_chart(b)
elif visualization=='Potential': 
  st.markdown("## **Energy Generation By State**")
  state = st.selectbox('Select state',df5['State'].unique())
  selected = df5[df5['State']==state]
  c=px.bar(selected,x='YearValue',y='Capacity_MW',color='EnergySource',barmode='group')
  st.plotly_chart(c)
  st.markdown("## **Energy Generation By Source**")
  energy_select=st.radio('Select a Energy Type',df4['EnergySourceType'].unique())
  energy=df4[df4['EnergySourceType']==energy_select]
  b=px.bar(energy,x='YearValue',y='CapacityIdentified_MW',color='EnergySource',barmode='group')
  st.plotly_chart(b)
  
