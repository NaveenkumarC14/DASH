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
df5=pd.read_csv('Electricity Potential by State_D_20210427_131321.csv')
df6=pd.read_csv('Electricity Capacity by State_D_20210427_143749.csv')
df7=pd.read_csv('Electricity Capacity by Energy Source_D_20210427_143811.csv')
st.sidebar.title("Energy")
visualization = st.sidebar.selectbox('Select a type',('Potential','Generation','Capacity','Insights'))
select_chart = st.sidebar.selectbox('Select a Chart',('Bar Chart','Bubble Chart','Pie'))
st.markdown('''
    <div class="jumbotron text-center" style='background-color: #fff'>
    <h1 style="margin: auto; width: 100%;">Current Energy Scenario in India</h1>
 
 
    </div>
''', unsafe_allow_html=True);
if visualization=='Generation':
  
 
  st.markdown("## **State wise Electricity Generation via Renewables**")
  state_select = st.selectbox('Select a state',df['State'].unique())
  
  selected_state = df[df['State']==state_select]
  if select_chart=='Bar Chart':
    a=px.bar(selected_state,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
    st.plotly_chart(a)
  elif select_chart=='Bubble Chart':
    Bubble=px.scatter(selected_state, x='YearValue', y='Generation_GWh',
	         size="Generation_GWh", color='EnergySource',size_max=60)
    st.plotly_chart(Bubble)
  elif select_chart=='Pie':
    a=px.pie(selected_state, values='Generation_GWh', names='EnergySource')
    st.plotly_chart(a)
	
	
  st.markdown("## **Generation of Electricity By Energy Source**")
  energy_select=st.radio('Select a Energy Type',df1['EnergySourceType'].unique())
  energy=df1[df1['EnergySourceType']==energy_select]
  if select_chart=='Bar Chart':
    b=px.bar(energy,x='YearValue',y='Generation_GWh',color='EnergySource',barmode='group')
    st.plotly_chart(b)
  elif select_chart=='Bubble Chart':
    Bubble=px.scatter(energy, x='YearValue', y='Generation_GWh',
	         size="Generation_GWh", color='EnergySource',size_max=60)
    st.plotly_chart(Bubble)
  elif select_chart=='Pie':
    a=px.pie(energy, values='Generation_GWh', names='EnergySource')
    st.plotly_chart(a)
	
	
  st.markdown("## **Total Electricity Generated by State**")
  state = st.selectbox('Select state',df2['State'].unique())
  selected = df2[df2['State']==state]
  if select_chart=='Bar Chart':
    c=px.bar(selected,x='YearValue',y='Generation_GWh')
    st.plotly_chart(c)
  elif select_chart=='Bubble Chart':
    c=px.scatter(selected,x='YearValue',y='Generation_GWh',size="Generation_GWh",size_max=60)
    st.plotly_chart(c)
  elif select_chart=='Pie':
    a=px.pie(selected, values='Generation_GWh', names='YearValue')
    st.plotly_chart(a)	
	
	
elif visualization=='Capacity':
  st.markdown("## **Installed Capacity by State**")
  state_select = st.selectbox('Select a state',df3['State'].unique())
  selected_state = df3[df3['State']==state_select]
  if select_chart=='Bar Chart':
    a=px.bar(selected_state,x='YearValue',y='Capacity_MW',color='EnergySource',barmode='group')
    st.plotly_chart(a)
  elif select_chart=='Bubble Chart':
    a=px.scatter(selected_state,x='YearValue',y='Capacity_MW',size="Capacity_MW",color='EnergySource',size_max=60)
    st.plotly_chart(a)
  elif select_chart=='Pie':
    a=px.pie(selected_state, values='Capacity_MW', names='YearValue')
    st.plotly_chart(a)	
	
	
  st.markdown("## **Installed Capacity by Energy Source**")
  energy_select=st.radio('Select a Energy Type',df7['EnergySourceType'].unique())
  energy=df7[df7['EnergySourceType']==energy_select]
  if select_chart=='Bar Chart':
    b=px.bar(energy,x='YearValue',y='Capacity_MW',color='EnergySource',barmode='group')
    st.plotly_chart(b)
  elif select_chart=='Bubble Chart':
    b=px.scatter(energy,x='YearValue',y='Capacity_MW',size="Capacity_MW",color='EnergySource',size_max=60)
    st.plotly_chart(b)
  elif select_chart=='Pie':
    a=px.pie(energy, values='Capacity_MW', names='YearValue')
    st.plotly_chart(a)	  
	
	
elif visualization=='Potential': 
  st.markdown("## **State Wise Potential **")
  state = st.selectbox('Select state',df5['State'].unique())
  selected = df5[df5['State']==state]
  if select_chart=='Bar Chart':
    c=px.bar(selected,x='YearValue',y='CapacityIdentified_MW')
    st.plotly_chart(c)
  elif select_chart=='Bubble Chart':
    b=px.scatter(selected,x='YearValue',y='CapacityIdentified_MW',size="CapacityIdentified_MW",size_max=60)
    st.plotly_chart(b)
  elif select_chart=='Pie':
    a=px.pie(selected, values='CapacityIdentified_MW', names='YearValue')
    st.plotly_chart(a)
	
  st.markdown("## **Energy Source Wise Potential**")
  energy_select=st.radio('Select a Energy Type',df4['EnergySourceType'].unique())
  energy=df4[df4['EnergySourceType']==energy_select]
  if select_chart=='Bar Chart':
    b=px.bar(energy,x='YearValue',y='CapacityIdentified_MW',color='EnergySource',barmode='group')
    st.plotly_chart(b)
  elif select_chart=='Bubble Chart':
    b=px.scatter(energy,x='YearValue',y='CapacityIdentified_MW',size="CapacityIdentified_MW",color='EnergySource',size_max=60)
    st.plotly_chart(b)
  elif select_chart=='Pie':
    a=px.pie(energy, values='CapacityIdentified_MW', names='YearValue')
    st.plotly_chart(a)
elif visualization=='Insights': 
  st.markdown('''
    <div class="jumbotron text-center" style='background-color: #fff'>
    <h1 style="margin: auto; width: 100%;">INSIGHTS FROM ANALYSIS IN ENERGY DOMAIN</h1>
 
 
    </div>
''', unsafe_allow_html=True);
  st.markdown(
  """
1. India is the 4th largest consumer of energy , 5th in energy economy and ranked 3rd on renewable energy investment and future plans. India ranked 5th for overall installed renewable energy capacity.

2. Govt targeted to achieve 175GW renewable energy capacity by 2022.

3. Primary energy consumption(Non-renewables) grew fastest since 2006. And Coal stands as the largest producer of energy since 2006 to till date.

4. All fuels grew faster than their 10 year averages apart from renewables, although renewables still accounted for the second largest increment to energy growth.

5. Renewable energy has a share of 23.3% in the total installed generation capacity in the country till the initial stage of 2020.

6. Solar energy has had a rapid growth in the last 5-6 years from 2.6GW to 34GW. Solar park has been doubled from 20GW to 40GW.

7. Since 2008 Wind Energy has kick-started its growth. As an extremity highest ever wind energy has been generated in the year 2016-17 by addition of 5.5GW, which is 57.52% of total energy generated in the particular year.

8. In the last 2 years Karnataka has generated the highest energy including renewables.

9. In last 4 years Tamil Nadu shows a good improvement in generation of energy including renewables like wind and solar. Tamil Nadu has wind potential as its highest among other renewables.

10. Rajasthan has the highest potential in Solar energy and the 2nd highest potential in Wind energy. Gujarat has the highest potential in wind energy.
  """
   )
  st.markdown('''
    <div class="jumbotron text-center" style='background-color: #fff'>
    <h1></h1>
    <h2 style="margin: auto; width: 100%;">OUT-OF-BOX INSIGHTS RELATING OTHER DOMAINS</h2>
 
 
    </div>
''', unsafe_allow_html=True);
  st.markdown(
  """
  **Health care :**

Renewable energy growth has a huge positive impact on people's health and there are reduced health and environmental hazards whereas the non-renewables are quite hazardous to health.

**Employment :**

Development of the renewable energy sector would bring greater average job creation as it requires more labour than its fossil fuel counterpart.

**Economy :**

Opting for renewable energy sources will lead to a lower impact of the global oil prices on Indian economy.

**Climate :**

Non-renewables currently being the largest electricity producer is hazardous to the climatic conditions and environment. It is possible to make electricity from renewables without producing carbon dioxide the leading cause of global climate change.
"""
   )
