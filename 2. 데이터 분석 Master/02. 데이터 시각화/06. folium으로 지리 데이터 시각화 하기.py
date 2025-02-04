# **folium으로 지리 데이터 시각화하기**


#서울시의 이디야, 투썸플레이스 위치를 시각화하고 두 카페의 지리적 분포가 어떻게 다른지 시각화를 통해 살펴봅시다.

import json
import folium
import pandas as pd


## **[1] 서울시 구별 경계 데이터 가져오기**

# [서울시 구별 경계 데이터](https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo.json)

geo_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\seoul_municipalities_geo_simple.json"
geo_json = json.load(open(geo_path, encoding='utf-8')) 

## **[2] 서울시 상가 정보 데이터 가져오기**
# [공공데이터포털](https://www.data.go.kr/data/15083033/fileData.do)

df = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\소상공인시장진흥공단_상가(상권)정보_서울_202306.csv", low_memory=False)
print(df.info())

## **[3] 카페별로 데이터를 전처리하고 EDA하기**

cafe = df.query('상권업종소분류명 == "카페"')

ediya = cafe.loc[cafe['상호명'].str.contains('이디야'),]
print(ediya)

twosome = cafe.loc[cafe['상호명'].str.contains('투썸플레이스'),]
print(twosome)

ediya_count = ediya.groupby('시군구명').size().to_frame().reset_index().rename({0:'count'}, axis=1).sort_values('count', ascending=False)
print(ediya_count)

twosome_count = twosome.groupby('시군구명').size().to_frame().reset_index().rename({0:'count'}, axis=1).sort_values('count', ascending=False)
print(twosome_count)


import plotly.express as px

fig = px.bar(data_frame=ediya_count, x='시군구명', y='count', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white', text_auto=True, title='서울시 구별 이디야 점포수')
'''fig.show()'''

fig = px.bar(data_frame=twosome_count, x='시군구명', y='count', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white', text_auto=True, title='서울시 구별 투썸플레이스 점포수')
'''fig.show()'''

## **[4] folium으로 지도에 시각화하기**

f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)
print(m)

folium.Choropleth(geo_data = geo_json, fill_color = 'gray').add_to(m)
print(m)

f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)
folium.Choropleth(geo_data = geo_json
                  , data=ediya_count
                  , columns=['시군구명', 'count']
                  , key_on='properties.name'
                  , fill_color = 'YlGn'
                  , fill_opacity = 0.7
                  , line_opacity = 0.7
                  , legend_name = '서울시 구별 이디야 매장수').add_to(m)
print(m)

f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)
folium.Choropleth(geo_data = geo_json
                  , data=twosome_count
                  , columns=['시군구명', 'count']
                  , key_on='properties.name'
                  , fill_color = 'BuPu'
                  , fill_opacity = 0.7
                  , line_opacity = 0.7
                  , legend_name = '서울시 구별 투썸플레이스 매장수').add_to(m)
print(m)

ediya_twosome = ediya_count.merge(twosome_count, on='시군구명', suffixes=('_이디야','_투썸'))
ediya_twosome['이디야_ratio'] = ediya_twosome['count_이디야'] / ediya_twosome['count_이디야'].sum()
ediya_twosome['투썸_ratio'] = ediya_twosome['count_투썸'] / ediya_twosome['count_투썸'].sum()
ediya_twosome['투썸 상대적 비율'] = ediya_twosome['투썸_ratio'] / ediya_twosome['이디야_ratio']

print(ediya_twosome)

f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)
folium.Choropleth(geo_data = geo_json
                  , data=ediya_twosome
                  , columns=['시군구명', '투썸 상대적 비율']
                  , key_on='properties.name'
                  , fill_color = 'RdPu'
                  , fill_opacity = 0.7
                  , line_opacity = 0.7
                  , legend_name = '서울시 구별 투썸 상대적 비율').add_to(m)
print(m)

ediya_df = ediya[['상호명','경도','위도']].copy()
ediya_df['kind'] = '이디야'

twosome_df = twosome[['상호명','경도','위도']].copy()
twosome_df['kind'] = '투썸'

dff = pd.concat([ediya_df, twosome_df])
print(dff.head())
print(dff.tail())


from _plotly_utils.basevalidators import TitleValidator
f = folium.Figure(width=700, height=500)
m = folium.Map(location=[37.566535, 126.9779692], zoom_start=11).add_to(f)

for idx in dff.index:
    lat = dff.loc[idx, '위도']
    long = dff.loc[idx, '경도']
    title = dff.loc[idx, '상호명']

    if dff.loc[idx, 'kind'] == "이디야":
        color = '#1d326c'
    else:
        color = '#D70035'
    folium.CircleMarker([lat, long]
                        , radius=3
                        , color = color
                        , tooltip = title).add_to(m)

print(m)