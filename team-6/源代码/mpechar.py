import pandas as pd
from pyecharts import Map
from pyecharts import Geo,Page
data=pd.read_excel('G:\\py_pro\\pollution2.xlsx')
cities=[]
PM25=[]
posi=[]

for i in data['city']:
	cities.append(i)
for i in data['PM2.5']:
    PM25.append(i)
i2=zip(cities,PM25)
z=zip(round(data['lng'],2),round(data['lat'],2))
for i in z:
	posi.append(list(i))
z2=dict(zip(cities,posi))

pages=Page()
my_map1=Geo('全国部分城市PM2.5情况分布',width=1200,height=600,background_color="#404a59",title_color="#fff",title_pos="center")
my_map1.add('',cities,data['PM2.5'],title_color="#fff",
    title_pos="center",maptype='china',symbol_size=10,geo_cities_coords=z2,
	type='scatter',is_visualmap=True,visual_range=[min(data['PM2.5']),max(data['PM2.5'])],
	is_piecewise=True,visual_text_color="#fff",is_label_emphasis=True,label_formatter='{b}')
pages.add_chart(my_map1)

my_map2=Geo('全国部分城市PM10情况分布',width=1200,height=600,background_color="#404a59",title_color="#fff",title_pos="center")
my_map2.add('',cities,data['PM10'],maptype='china',symbol_size=10,geo_cities_coords=z2,title_color="#fff",
    title_pos="center",type='scatter',is_visualmap=True,visual_range=[min(data['PM10']),max(data['PM10'])],
	is_piecewise=True,visual_text_color="#fff",is_label_emphasis=True,label_formatter='{b}')
pages.add_chart(my_map2)

my_map3=Geo('全国部分城市O3情况分布',width=1200,height=600,background_color="#404a59",title_color="#fff",title_pos="center")
my_map3.add('',cities,data['O3'],maptype='china',symbol_size=10,geo_cities_coords=z2,visual_range=[min(data['O3']),max(data['O3'])],type='scatter',is_visualmap=True,
	is_piecewise=True,visual_text_color="#fff",is_label_emphasis=True,label_formatter='{b}')
pages.add_chart(my_map3)	
	
my_map4=Geo('全国部分城市NO2情况分布',width=1200,height=600,background_color="#404a59",title_color="#fff",title_pos="center")
my_map4.add('',cities,data['NO2'],maptype='china',symbol_size=10,geo_cities_coords=z2,visual_range=[min(data['NO2']),max(data['NO2'])],
	type='scatter',is_visualmap=True,title_color="#fff",title_pos="center",
	is_piecewise=True,visual_text_color="#fff",is_label_emphasis=True,label_formatter='{b}')
pages.add_chart(my_map4)

my_map5=Geo('全国部分城市SO2情况分布',width=1200,height=600,background_color="#404a59",title_color="#fff",title_pos="center")
my_map5.add('',cities,data['SO2'],maptype='china',symbol_size=10,geo_cities_coords=z2,title_color="#fff",title_pos='center',
	type='scatter',is_visualmap=True,visual_range=[min(data['SO2']),max(data['SO2'])],
	is_piecewise=True,visual_text_color="#fff",is_label_emphasis=True,label_formatter='{b}')
pages.add_chart(my_map5)

pages.render()
