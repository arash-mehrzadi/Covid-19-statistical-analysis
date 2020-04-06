# Covid-19-statistical-analysis
<img src="/Temp(Not_Important)/screenshots/s2.png" width="whatever" height="whatever">

# Detail

### methods

| Metods  | Details |
| ------------- | ------------- |
| Geographical Charts  | Statistical analysis of cities' mortality distribution and implementation of results on geographic maps |
| Treemap   | Analysis of statistical data on the dead, recovered and people with the Corona virus  |
| Bubble Geomap   | plot coronavirus Death cases spread on Geomap using Basemap |

# Bubble Geomap 

![](/Temp(Not_Important)/Gifs/Bubble_Geomap_GIF.gif)

In this section I used[Dataset_LAT_LON_cumsum.csv](https://github.com/arash-mehrzadi/Covid-19-statistical-analysis/blob/master/Data/Dataset_LAT_LON_cumsum.csv) , The dataset contains reports of deaths from coronavirus and improved numbers of patients. These data have been collected separately from 32 provinces of Iran and the geographical location of the provinces added to work with geographical charts . I have used this data to plot the geographic distribution of the Corona virus casualties .

# Geographical Charts

![](/Temp(Not_Important)/Gifs/GeoMapGif.gif)

In this section I used statistical data, including casualties due to the outbreak of the Korona virus in Iran, recorded in different cities and updated the results of my assessments, which included a detailed analysis of 31 provinces of Iran on a daily basis. I published a geographic map.

# Treemap

<img src="/iran/treemap/Plots_PNG/2020-03-26/All_province_Active.png" width="1000">

In this section of the Treemap chart, I have implemented these charts both regionally for the analysis of the death toll in different provinces of Iran and for the analysis of corona virus deaths, remedies, and patients with definitive corona symptoms.

# Requirements

This codes is built using Python 3.7.5, and utilizes the following packages;

- GeoPandas 0.7.0
- pandas 1.0.3
- matplotlib 3.2.1
- basemav 1.1.0
