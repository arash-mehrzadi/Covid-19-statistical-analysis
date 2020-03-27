# -*- coding: utf-8 -*-
"""
Geographical Distribution
         of
    Corona Mortality
"""

import pandas as pd
import geopandas as gpd
import matplotlib as plt

d = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [17.0,249.0,36.0,60.0,0.0,10.0,29.0,87.0,26.0,2.0,0.0,2.0,0.0,38.0,19.0,57.0,28.0,16.0,28.0,36.0,7.0,22.0,19.0,33.0,17.0,42.0,15.0,84.0,15.0,8.0,26.0]}

logy_dataframe = pd.DataFrame(data=d)

print("---------------------------------------",logy_dataframe,"---------------------------------------------",sep="\n)




map_df = gpd.read_file("Covid-19/IranGeo/IRN_adm1.shp")


print("---------------------------------------",map_df['NAME_1'],"---------------------------------------------",sep="\n)

map_df.plot()

print("---------------------------------------",logy_dataframe,"---------------------------------------------",sep="\n)



merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))

merged.plot(column='unemp',cmap='Reds',edgecolor='0.1',figsize=(15, 15))

variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('IRAN Geographical distribution', fontdict={'fontsize': '25', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)

"""# section 2"""


idf = pd.read_csv('Covid-19/data/province(iran)(2020-03-22).csv')


print("---------------------------------------",idf,"---------------------------------------------",sep="\n)


print("---------------------------------------",idf[0:1],"---------------------------------------------",sep="\n)


df=pd.DataFrame()

i=1
Daylist=list(range(0,33))
while i<=32:
   #print(idf[0:i].sum())
   Daylist[i]=idf[0:i].sum()
   #print(Text)
   i+=1

TID = Daylist[1]



clist=['Qom', 'Tehran', 'Mazandaran', 'Alburz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Koh_boyr','Charmahal' ,'Bushehr' ,'Gilan', 'Ardebil', 'East_Azerbaijan', 'West_Azerbaijan', 'Kurdestan','Zanjan' ,'Markazi' ,'Hamedan', 'Khuzistan', 'Kermanshah', 'Lorstan', 'Ilam','Razavi_Khr' ,'Sis_baluchestan' ,'Yazd','South_Khs' ,'Kerman' ,'North_Khn']

for i in clist:
  print(TID[i])

Day=1
while Day<=32:
  TID=Daylist[Day]
  print("------------------------------",Day,"------------------------------------")
  Day+=1
  for i in clist:
    print(TID[i],end=',')

d1 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d2 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d3 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [11.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d4 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [19.0,6.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d5 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [26.0,10.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.0,0.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d6 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [34.0,13.0,1.0,0.0,0.0,0.0,0.0,2.0,0.0,0.0,0.0,0.0,0.0,6.0,0.0,0.0,0.0,0.0,0.0,4.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]}


d7 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [50.0,21.0,3.0,2.0,0.0,0.0,0.0,2.0,1.0,1.0,0.0,0.0,0.0,8.0,0.0,0.0,0.0,0.0,0.0,4.0,1.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0,0.0]}


d8 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [65.0,25.0,4.0,2.0,1.0,0.0,0.0,2.0,3.0,2.0,2.0,0.0,0.0,9.0,0.0,0.0,0.0,0.0,0.0,5.0,1.0,3.0,1.0,1.0,0.0,1.0,2.0,0.0,0.0,0.0,0.0]}


d9 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [72.0,63.0,11.0,5.0,4.0,0.0,0.0,10.0,3.0,2.0,2.0,0.0,0.0,32.0,5.0,2.0,1.0,1.0,0.0,5.0,2.0,3.0,3.0,4.0,0.0,2.0,2.0,1.0,0.0,0.0,0.0]}


d10 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [88.0,127.0,20.0,8.0,6.0,2.0,2.0,20.0,3.0,2.0,2.0,0.0,0.0,57.0,6.0,6.0,1.0,3.0,0.0,5.0,2.0,6.0,3.0,4.0,0.0,2.0,2.0,1.0,0.0,0.0,0.0]}


d11 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [109.0,179.0,32.0,16.0,10.0,24.0,8.0,32.0,11.0,2.0,2.0,0.0,0.0,74.0,9.0,12.0,1.0,8.0,0.0,23.0,2.0,10.0,3.0,4.0,1.0,2.0,3.0,5.0,1.0,0.0,0.0]}


d12 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [139.0,349.0,43.0,47.0,13.0,24.0,8.0,45.0,19.0,4.0,2.0,0.0,0.0,102.0,9.0,12.0,1.0,8.0,0.0,67.0,5.0,19.0,5.0,12.0,2.0,19.0,5.0,5.0,3.0,2.0,0.0]}


d13 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [139.0,349.0,43.0,47.0,13.0,24.0,8.0,45.0,19.0,4.0,2.0,0.0,0.0,102.0,9.0,12.0,1.0,8.0,0.0,67.0,5.0,19.0,5.0,12.0,2.0,19.0,5.0,5.0,3.0,2.0,0.0]}


d14 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [139.0,349.0,43.0,47.0,13.0,24.0,8.0,45.0,19.0,4.0,2.0,0.0,0.0,102.0,9.0,12.0,1.0,8.0,0.0,67.0,5.0,19.0,5.0,12.0,2.0,19.0,5.0,5.0,3.0,2.0,0.0]}


d15 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [240.0,602.0,52.0,66.0,21.0,33.0,33.0,45.0,33.0,4.0,2.0,1.0,0.0,137.0,9.0,21.0,1.0,12.0,6.0,75.0,5.0,46.0,20.0,17.0,9.0,27.0,13.0,5.0,3.0,16.0,1.0]}


d16 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [272.0,658.0,102.0,127.0,43.0,37.0,64.0,163.0,52.0,6.0,2.0,9.0,3.0,217.0,26.0,31.0,6.0,18.0,13.0,106.0,11.0,47.0,20.0,28.0,9.0,80.0,18.0,5.0,12.0,16.0,3.0]}


d17 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [409.0,719.0,282.0,256.0,97.0,104.0,129.0,313.0,65.0,12.0,6.0,14.0,5.0,308.0,37.0,41.0,7.0,42.0,48.0,154.0,18.0,47.0,25.0,78.0,11.0,80.0,20.0,55.0,15.0,23.0,15.0]}


d18 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [554.0,845.0,587.0,259.0,121.0,162.0,131.0,409.0,79.0,23.0,6.0,16.0,8.0,378.0,38.0,43.0,29.0,44.0,50.0,191.0,29.0,48.0,29.0,105.0,13.0,126.0,33.0,79.0,15.0,38.0,23.0]}


d19 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [571.0,1111.0,601.0,261.0,158.0,175.0,160.0,489.0,88.0,28.0,9.0,21.0,10.0,380.0,47.0,73.0,36.0,63.0,51.0,261.0,55.0,53.0,31.0,142.0,13.0,145.0,33.0,85.0,41.0,39.0,24.0]}


d20 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [598.0,1251.0,614.0,261.0,203.0,175.0,200.0,526.0,117.0,45.0,9.0,26.0,11.0,408.0,69.0,95.0,65.0,66.0,66.0,315.0,55.0,57.0,42.0,149.0,29.0,174.0,33.0,88.0,34.0,34.0,34.0]}


d21 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [637.0,1420.0,867.0,293.0,204.0,179.0,210.0,543.0,135.0,62.0,11.0,37.0,18.0,408.0,88.0,112.0,69.0,78.0,77.0,342.0,72.0,94.0,49.0,174.0,54.0,213.0,39.0,125.0,48.0,38.0,34.0]}


d22 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [690.0,1676.0,899.0,338.0,267.0,188.0,237.0,713.0,154.0,72.0,11.0,38.0,18.0,413.0,89.0,141.0,96.0,84.0,99.0,373.0,79.0,111.0,57.0,183.0,60.0,247.0,43.0,148.0,63.0,56.0,45.0]}


d23 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [732.0,1979.0,978.0,412.0,307.0,213.0,279.0,717.0,183.0,72.0,26.0,49.0,21.0,497.0,103.0,148.0,115.0,93.0,116.0,461.0,91.0,142.0,77.0,208.0,67.0,276.0,49.0,169.0,75.0,63.0,45.0]}


d24 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [774.0,2282.0,1170.0,418.0,345.0,234.0,291.0,827.0,216.0,76.0,26.0,49.0,21.0,568.0,118.0,245.0,140.0,102.0,136.0,509.0,101.0,157.0,92.0,233.0,75.0,386.0,51.0,215.0,75.0,75.0,87.0]}


d25 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [806.0,2629.0,1187.0,552.0,392.0,234.0,338.0,982.0,227.0,76.0,26.0,49.0,28.0,681.0,151.0,304.0,171.0,107.0,167.0,624.0,108.0,205.0,100.0,235.0,81.0,416.0,53.0,288.0,79.0,75.0,88.0]}


d26 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [890.0,2880.0,1259.0,619.0,433.0,259.0,360.0,1108.0,236.0,83.0,27.0,49.0,34.0,724.0,151.0,340.0,189.0,134.0,199.0,624.0,119.0,237.0,113.0,287.0,99.0,559.0,59.0,324.0,97.0,82.0,94.0]}


d27 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [909.0,3080.0,1355.0,668.0,467.0,301.0,400.0,1226.0,279.0,99.0,32.0,52.0,38.0,742.0,181.0,375.0,220.0,165.0,214.0,638.0,131.0,290.0,129.0,287.0,101.0,559.0,70.0,375.0,104.0,95.0,139.0]}


d28 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [938.0,3353.0,1414.0,784.0,500.0,331.0,426.0,1301.0,310.0,105.0,32.0,54.0,42.0,787.0,200.0,453.0,254.0,167.0,239.0,685.0,137.0,315.0,143.0,322.0,108.0,622.0,81.0,424.0,116.0,114.0,142.0]}


d29 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [960.0,3566.0,1475.0,860.0,560.0,351.0,479.0,1463.0,370.0,117.0,45.0,58.0,46.0,808.0,210.0,537.0,296.0,189.0,259.0,708.0,150.0,343.0,150.0,361.0,118.0,652.0,87.0,469.0,137.0,125.0,142.0]}


d30 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [991.0,3703.0,1533.0,921.0,576.0,360.0,526.0,1571.0,391.0,122.0,60.0,61.0,54.0,881.0,226.0,595.0,322.0,200.0,285.0,755.0,153.0,365.0,173.0,398.0,126.0,702.0,105.0,538.0,142.0,139.0,163.0]}


d31 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [1027.0,3923.0,1617.0,1016.0,628.0,375.0,534.0,1716.0,441.0,139.0,61.0,64.0,55.0,980.0,261.0,650.0,349.0,215.0,329.0,772.0,158.0,375.0,195.0,407.0,146.0,750.0,113.0,587.0,160.0,151.0,180.0]}


d32 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': []}


d33 = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [1047.0,4155.0,1645.0,1071.0,628.0,381.0,593.0,1817.0,463.0,139.0,73.0,66.0,55.0,1037.0,267.0,722.0,363.0,222.0,364.0,772.0,163.0,406.0,222.0,441.0,164.0,807.0,118.0,639.0,160.0,159.0,181.0]}


logy_dataframe = pd.DataFrame(data=d1)


map_df = gpd.read_file("Covid-19/IranGeo/IRN_adm1.shp")

merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))

variable = 'unemp'
vmin, vmax = 0, 5000
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d2)

merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))

variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d3)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d4)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d5)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d5)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d6)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d4)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d8)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d9)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d10)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d11)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d12)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d13)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d14)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d15)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d16)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d17)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d18)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d19)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d20)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d21)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d22)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d23)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d24)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d25)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d26)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d27)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d28)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d29)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d30)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)



logy_dataframe = pd.DataFrame(data=d31)
merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))
variable = 'unemp'
vmin, vmax = 0, 300
fig, ax = plt.pyplot.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Geographical Distribution \nof \nCorona Mortality', fontdict={'fontsize': '15', 'fontweight' : '3'})
ax.annotate('Source: https://github.com/arash-mehrzadi/Covid-19-statistical-analysis',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12, color='#555555')
sm = plt.pyplot.cm.ScalarMappable(cmap='Reds', norm=plt.pyplot.Normalize(vmin=vmin, vmax=vmax))
sm._A = []
#cbar = fig.colorbar(sm)
merged.plot(column='unemp',cmap='OrRd',edgecolor='0.1',ax=ax, legend=True)

#end
