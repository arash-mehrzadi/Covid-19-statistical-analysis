# -*- coding: utf-8 -*-

import pandas as pd


Da_Fr = pd.read_csv('/content/drive/My Drive/Covid-19/data/province(iran)(2020-03-22).csv')


Wcitylist = ['Qom', 'Tehran', 'Mazandaran', 'Alburz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Koh_boyr','Charmahal' ,'Bushehr' ,'Gilan', 'Ardebil', 'East_Azerbaijan', 'West_Azerbaijan', 'Kurdestan','Zanjan' ,'Markazi' ,'Hamedan', 'Khuzistan', 'Kermanshah', 'Lorstan', 'Ilam','Razavi_Khr' ,'Sis_baluchestan' ,'Yazd','South_Khs' ,'Kerman' ,'North_Khn']



Tcitylist = ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan']

print(len(Wcitylist))
print("---------------Non-standard----------------",len(Wcitylist),"--------------------------------",sep="\n")
print("-----------------standard------------------",len(Tcitylist),"--------------------------------",sep="\n")

print("-----------------Non-conforming------------------","-------->>>><<<<--------",sep="\n")

for i in range(0,31):
  if not (Wcitylist[i]==Tcitylist[i]):
    print(i)
    

print("---------<<<<>>>>>----------")

TDAF = Da_Fr.rename(columns={Wcitylist[3]:Tcitylist[3],Wcitylist[10]:Tcitylist[10],Wcitylist[11]:Tcitylist[11],Wcitylist[15]:Tcitylist[15],Wcitylist[16]:Tcitylist[16],Wcitylist[17]:Tcitylist[17],Wcitylist[20]:Tcitylist[20],Wcitylist[21]:Tcitylist[21],Wcitylist[23]:Tcitylist[23],Wcitylist[25]:Tcitylist[25],Wcitylist[26]:Tcitylist[26],Wcitylist[28]:Tcitylist[28],Wcitylist[30]:Tcitylist[30]})





Date_series = TDAF['Date'].to_list()

for i in range(0,33):
  print(Date_series[i])

Date_series = ['2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22',
'2020/02/19',
'2020/02/20',
'2020/02/21',
'2020/02/22',
'2020/02/23',
'2020/02/24',
'2020/02/25',
'2020/02/26',
'2020/02/27',
'2020/02/28',
'2020/02/29',
'2020/03/01',
'2020/03/02',
'2020/03/03',
'2020/03/04',
'2020/03/05',
'2020/03/06',
'2020/03/07',
'2020/03/08',
'2020/03/09',
'2020/03/10',
'2020/03/11',
'2020/03/12',
'2020/03/13',
'2020/03/14',
'2020/03/15',
'2020/03/16',
'2020/03/17',
'2020/03/18',
'2020/03/19',
'2020/03/20',
'2020/03/21',
'2020/03/22']


citylist = ['Qom',
 'Tehran',
 'Mazandaran',
 'Alborz',
 'Semnan' ,
 'Golestan' ,
 'Qazvin',
 'Esfahan',
 'Fars',
 'Hormozgan',
 'Kohgiluyeh and Buyer Ahmad',
 'Chahar Mahall and Bakhtiari' ,
 'Bushehr' ,'Gilan', 'Ardebil',
 'East Azarbaijan',
 'West Azarbaijan',
 'Kordestan','Zanjan' ,
 'Markazi' ,
 'Hamadan',
 'Khuzestan',
 'Kermanshah',
 'Lorestan',
 'Ilam',
 'Razavi Khorasan' ,
 'Sistan and Baluchestan' ,
 'Yazd','South Khorasan' ,
 'Kerman' ,
 'North Khorasan']



TDAF = TDAF[['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan']]



"""# New Iaa"""

RDATA = []
for i in citylist:
  DATAPROV = TDAF[i].tolist()
  RDATA.append(DATAPROV)


provlist = []
for i in citylist:
  for a in range(0,33):
    provlist.append(i)

d = {'city': provlist, 'Date' : Date_series}
df = pd.DataFrame(data=d)

df['Death']=RDATA[0]+RDATA[1]+RDATA[2]+RDATA[3]+RDATA[4]+RDATA[5]+RDATA[6]+RDATA[7]+RDATA[8]+RDATA[9]+RDATA[10]+RDATA[11]+RDATA[12]+RDATA[13]+RDATA[14]+RDATA[15]+RDATA[16]+RDATA[17]+RDATA[18]+RDATA[19]+RDATA[20]+RDATA[21]+RDATA[22]+RDATA[23]+RDATA[24]+RDATA[25]+RDATA[26]+RDATA[27]+RDATA[28]+RDATA[29]+RDATA[30]

df[df['city']=='Tehran']


"""# 222"""

df.to_csv('Updated_Dataset.csv')