# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd


lats = np.array([34.654461, 35.689198, 36.947979, 35.876431, 35.578350, 36.8392776, 36.2804074, 32.6707877,29.299051,27.7198095,30.655874150000002,32.0163307,28.9310786,37.5115476,38.286843000000005,38.0544265,37.7416484,36.6944588,36.6699809,34.5302705,34.973321,31.5535141,34.3239414,33.5372643,33.611179,35.756361,28.1292481,31.8886686,33.0006776,30.2924085,37.5378855])
lons = np.array([50.879280, 51.388973, 53.285690, -78.749481, 53.387699, 54.4320858, 50.006663, 51.6650002,53.218456,56.335807,51.59954229916475,50.685709,50.8458443,49.355442984970665,48.14670296064578,46.34480692830047,45.0207638,45.1448828,48.4859398,49.7864561,48.6555779,49.0077168,47.0735891,48.2435197,46.06133080641574,59.1280992,60.8236848,54.3641264,58.3262335,57.0645647,56.9526137])


print("--------------Latitude_Len-----------------",len(lats),"--------------------------------",sep="\n")
print("--------------Longitude_len-----------------",len(lons),"--------------------------------",sep="\n")



MyDATAFRAME = pd.read_csv('/content/drive/My Drive/Updated_Dataset.csv')

MyDATAFRAME
print("--------------Dataframe_info_before-----------------",MyDATAFRAME.info(),"--------------------------------",sep="\n")



for i in lats:
  for a in range(0,33):
    latlist.append(i)

lonlist = []
for i in lons:
  for a in range(0,33):
    lonlist.append(i)
    

MyDATAFRAME['Latitude']=latlist

MyDATAFRAME['Longitude']=lonlist

MyDATAFRAME = MyDATAFRAME.drop(['Unnamed: 0'],axis=1)

MyDATAFRAME['Death'] = MyDATAFRAME['Death'].fillna(0)

print("--------------Dataframe_info_after-----------------",MyDATAFRAME.info(),"--------------------------------",sep="\n")



pluscash = MyDATAFRAME[MyDATAFRAME['city']=='Qom']

citylist = ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan']

loosum =[]
for i in citylist:
  pluscash = MyDATAFRAME[MyDATAFRAME['city']==i]
  loosum.append(pluscash['Death'].cumsum().to_list())

DeathRecord =[]
DeathRecord = loosum[0]+loosum[1]+loosum[2]+loosum[3]+loosum[4]+loosum[5]+loosum[6]+loosum[7]+loosum[8]+loosum[9]+loosum[10]+loosum[11]+loosum[12]+loosum[13]+loosum[14]+loosum[15]+loosum[16]+loosum[17]+loosum[18]+loosum[19]+loosum[20]+loosum[21]+loosum[22]+loosum[23]+loosum[24]+loosum[25]+loosum[26]+loosum[27]+loosum[28]+loosum[29]+loosum[30]

NewFinalDataFrame = MyDATAFRAME[['city','Date','Latitude','Longitude']]

NewFinalDataFrame['Death']=DeathRecord

NewFinalDataFrame.to_csv('Dataset_LAT_LON_cumsum.csv') 
