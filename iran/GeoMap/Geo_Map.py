import pandas as pd
import geopandas as gpd
import matplotlib as plt


map_df = gpd.read_file('Covid-19/IranGeo/IRN_adm1.shp')
print(map_df['NAME_1'],"------------------------------------------------------------","map_plot :",sep="\n")
map_df.plot()

d = {'fips': ['Qom', 'Tehran', 'Mazandaran', 'Alborz','Semnan' ,'Golestan' ,'Qazvin', 'Esfahan', 'Fars', 'Hormozgan', 'Kohgiluyeh and Buyer Ahmad','Chahar Mahall and Bakhtiari' ,'Bushehr' ,'Gilan', 'Ardebil', 'East Azarbaijan', 'West Azarbaijan', 'Kordestan','Zanjan' ,'Markazi' ,'Hamadan', 'Khuzestan', 'Kermanshah', 'Lorestan', 'Ilam','Razavi Khorasan' ,'Sistan and Baluchestan' ,'Yazd','South Khorasan' ,'Kerman' ,'North Khorasan'], 'unemp': [17.0,249.0,36.0,60.0,0.0,10.0,29.0,87.0,26.0,2.0,0.0,2.0,0.0,38.0,19.0,57.0,28.0,16.0,28.0,36.0,7.0,22.0,19.0,33.0,17.0,42.0,15.0,84.0,15.0,8.0,26.0]}


logy_dataframe = pd.DataFrame(data=d)
print("---------------Data_Frame----------------",logy_dataframe,"--------------------------------",sep="\n")

merged = map_df.set_index('NAME_1').join(logy_dataframe.set_index('fips'))


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