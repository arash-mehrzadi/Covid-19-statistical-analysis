import pandas as pd
import calmap
import plotly.express as px

irandataT = pd.read_csv('Covid-19/data/Iran(2020-03-24).csv')
print(irandataT,"---------------------------------------------------------",sep="\n")
print(irandataT.info(),"-------------------------------------------------------",sep="\n")

irandataT['Active']= irandataT['confirmed']-irandataT['deaths']-irandataT['recovered']
print(irandataT['Active'],"---------------------------------------------------------",sep="\n")

temp = irandataT.groupby('date')['Active', 'deaths', 'recovered'].sum().reset_index()
temp = temp[temp['date']==max(temp['date'])].reset_index(drop=True)
print(temp.style.background_gradient(cmap='Pastel1'),"--------------------------------------------",sep="/n")
tm = temp.melt(id_vars="date", value_vars=['Active', 'deaths', 'recovered'])
dth = '#ff2e63'
rec = '#21bf73' 
act = '#fe9801'
fig = px.treemap(tm, path=["variable"], values="value", height=400, width=600, color_discrete_sequence=[rec, act, dth])
fig.show()
print("-----------------------------------------------------------------------------------")
irandataT_pvi = pd.read_csv("Covid-19/data/province(iran)(2020-03-22).csv")
print(irandataT_pvi,"---------------------------------------------------------",sep="\n")
print(irandataT_pvi.info(),"---------------------------------------------------------",sep="\n")
temp_pvi = irandataT_pvi.groupby('Date')['Qom', 'Tehran', 'Mazandaran', 'Alburz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Koh_boyr','Charmahal' ,'Bushehr' ,'Gilan', 'Ardebil', 'East_Azerbaijan', 'West_Azerbaijan', 'Kurdestan','Zanjan' ,'Markazi' ,'Hamedan', 'Khuzistan', 'Kermanshah', 'Lorstan', 'Ilam','Razavi_Khr' ,'Sis_baluchestan' ,'Yazd','South_Khs' ,'Kerman' ,'North_Khn'].sum().reset_index()
temp_pvi = temp_pvi[temp_pvi['Date']==max(temp_pvi['Date'])].reset_index(drop=True)
print(temp_pvi.style.background_gradient(cmap='Pastel1'),"---------------------------------------------------",sep="\n")
tm = temp_pvi.melt(id_vars="Date", value_vars=['Qom', 'Tehran', 'Mazandaran', 'Alburz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Koh_boyr','Charmahal' ,'Bushehr' ,'Gilan', 'Ardebil', 'East_Azerbaijan', 'West_Azerbaijan', 'Kurdestan','Zanjan' ,'Markazi' ,'Hamedan', 'Khuzistan', 'Kermanshah', 'Lorstan', 'Ilam','Razavi_Khr' ,'Sis_baluchestan' ,'Yazd','South_Khs' ,'Kerman' ,'North_Khn'])
fig = px.treemap(tm, path=["variable"], values="value", height=700, width=900)
fig.show()