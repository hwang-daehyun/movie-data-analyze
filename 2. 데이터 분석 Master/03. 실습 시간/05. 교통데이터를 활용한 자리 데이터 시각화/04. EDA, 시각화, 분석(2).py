import pandas as pd
import plotly.express as px

data = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\Part3) 파이썬 데이터 분석 실습\\Data\\실습5_ 교통 데이터를 활용한 지리 데이터 시각화\\서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding = 'cp949')


#- 날짜 컬럼 추가
data['연도'] = pd.to_datetime(data['사용월'], format='%Y%m').dt.year
data['월'] = pd.to_datetime(data['사용월'], format='%Y%m').dt.month

#- 2018년 이후, 2호선만 필터링
data = data.query('연도 >= 2018').query('호선명 == "2호선"')
data = data.query('호선명 == "2호선" and 연도 >= 2018')

#- 지하철역명 통일
data['지하철역'] = [i[0] for i in data['지하철역'].str.split('(')]

#- 승차 인원만 추출하기
on_col = [i for i in data.columns if '승차' in i]
data = data[['사용월', '연도','월','지하철역']+on_col]

## **분석**
### [1] 승차 인원이 가장 많은 역은?
#- 합계 컬럼 만들기
data['합계'] = data[on_col].sum(axis=1)
'''print(data.head())'''

#- 지하철역별 월평균 승차 인원 구하기
data_mean = data.groupby('지하철역')[['합계']].mean().reset_index().rename({'합계' : '월평균'}, axis=1).sort_values('월평균', ascending=False)

fig = px.bar(data_frame=data_mean, x='지하철역', y='월평균', title='지하철역별 월평균 승차인원')
'''fig.show()'''

### [2] 연도별로 혹은 월별로 승차 인원 추이에 차이가 있는가?
# - 연도별
year_sum = data.query('연도 <=2022').groupby(['연도'])[['합계']].sum().reset_index()
year_sum['연도'] = year_sum['연도'].astype(str)
fig = px.line(data_frame=year_sum, x='연도', y='합계')
'''fig.show()'''

# - 월별
month_sum = data.query('연도 <= 2022').groupby(['월'])[['합계']].sum().reset_index()
month_sum['월'] = month_sum['월'].astype(str)
fig = px.line(data_frame=month_sum, x='월', y='합계')
'''fig.show()'''

### [3] 시간대별로 가장 승차인원이 많은 역은?

#주요 역 10개만 필터링하여 시간당 월평균 인원수 구하기
top10 = data_mean.sort_values('월평균', ascending=False).head(10)['지하철역']
top10_mean_hour = data.query('지하철역 in @top10').groupby('지하철역')[on_col].mean()
top10_mean_hour.columns = [i[:3] for i in top10_mean_hour.columns]

#전체 기준 히트맵
top10_mean_hour.style.background_gradient(cmap='pink_r', axis=None).format('{:.0f}')

#행 기준 히트맵
top10_mean_hour.style.background_gradient(cmap='pink_r', axis=1).format('{:.0f}')


### [4] 지하철역 시간대별 인원 유형 군집화

#- 승차 인원으로 유형 군집화
hour_mean = data.groupby('지하철역')[on_col].mean()
hour_mean.columns = [i[:3] for i in hour_mean.columns]
# 행별 합이 1이 되는 퍼센트를 만든다
hour_mean_pct = hour_mean.div(hour_mean.sum(axis=1), axis=0)

from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer

model = KMeans()
visualizer = KElbowVisualizer(model, k=(1,10))
visualizer.fit(hour_mean_pct)

k=3
model = KMeans(n_clusters = k, random_state = 10) # KMeans 모델을 정의
model.fit(hour_mean_pct) # fit을 통해 학습
hour_mean_pct['cluster'] = model.fit_predict(hour_mean_pct).astype(str) # 클러스터 열 만들기

fig = px.scatter(data_frame=hour_mean_pct[['08시','18시','cluster']].reset_index(), x='08시', y='18시', color='cluster', width=700, height=600, title='시간대별 승차 인원 비중 군집화', hover_name='지하철역')
'''fig.show()'''

'''for i in range(k):
    print(f'cluster {i}')
    print(list(hour_mean_pct.query(f'cluster == "{i}"').index)) '''

### [5] 지도에 분석 결과를 시각화

#-  8시 승차 인원과 18시 승차 인원을 지도에 시각화 해보자

#- 지하철역별 위도 경도 데이터 전처리

coordinate = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습5_ 교통 데이터를 활용한 지리 데이터 시각화\\서울시 역사마스터 정보.csv", encoding='cp949')
'''print(coordinate.head())'''

coordinate = coordinate.query('호선 == "2호선"')
coordinate['역사명'] = [i[0] for i in coordinate['역사명'].str.split('(')]
coordinate.rename({'역사명' : '지하철역'}, axis=1, inplace=True)

hour_mean_merge = hour_mean.reset_index()[['지하철역','08시','18시']]
coordinate_merge = coordinate[['지하철역','위도','경도']]
hour_mean_coor = pd.merge(hour_mean_merge, coordinate_merge, on='지하철역')
hour_mean_coor['cluster'] = model.fit_predict(hour_mean_pct).astype(str)
'''print(hour_mean_coor.head())'''

#- 지도에 시각화
import folium
from folium import plugins

center = [37.541, 126.986]

m = folium.Map(location=center, zoom_start=12)
m.add_child(plugins.HeatMap(zip(hour_mean_coor['위도'],hour_mean_coor['경도'], hour_mean_coor['08시'])))


#- 승차 인원 유형을 지도에 시각화
m = folium.Map(location=center, zoom_start=12)

for idx in hour_mean_coor.index:
    lat = hour_mean_coor.loc[idx, '위도']
    long = hour_mean_coor.loc[idx, '경도']
    title = hour_mean_coor.loc[idx, '지하철역']

    if hour_mean_coor.loc[idx, 'cluster'] == "0":
        color = '#000000'
    elif hour_mean_coor.loc[idx, 'cluster'] == "1":
        color = '#3A01DF'
    else:
        color = '#DF0101'

    folium.CircleMarker([lat, long]
                        , radius=18
                        , color = color
                        , fill = color
                        , tooltip = title).add_to(m)
    


## **정리**

#[1] 승하차 인원이 가장 많은 역은?
#- 강남, 잠실, 홍대입구, 신림, 구로디지털단지...

#[2] 연도별로 혹은 월별로 승차 인원 추이에 차이가 있는가?
#- 코로나가 시작된 2020년, 2021년에 인원이 많이 줄었고 2022년도부터 다시 회복 중

#[3] 시간대별로 가장 승차인원이 많은 역은?
#- 아침에 비교적 승차 인원이 많은 역과 저녁에 비교적 승차 인원이 많은 역이 있음을 히트맵으로 파악

#[4] 지하철역 시간대별 인원 유형 군집화

#    cluster 0: 아침과 저녁 승차인원 비율이 비교적 비슷
#    ['건대입구', '구로디지털단지', '당산', '도림천', '문래', '방배', '사당', '신당', '신도림', '신설동', '신촌', '영등포구청', '왕십리', '이대', '잠실', '종합운동장', '충정로', '합정', '홍대입구']
#    cluster 1: 저녁 승차인원 비율이 높음
#    ['강남', '교대', '동대문역사문화공원', '뚝섬', '삼성', '서초', '선릉', '성수', '시청', '역삼', '을지로3가', '을지로4가', '을지로입구', '한양대']
#    cluster 2: 아침 승차인원 비율이 높음
#    ['강변', '구의', '낙성대', '대림', '봉천', '상왕십리', '서울대입구', '신답', '신대방', '신림', '신정네거리', '아현', '양천구청', '용답', '용두', '잠실나루', '잠실새내']

#[5] 지도에 분석 결과를 시각화
#- cluster 0: 주거와 상업 시설, 회사가 비슷하게 분포한 지역
#- cluster 1: 회사가 많이 분포한 지역
#- cluster 2: 주거 지역이 많이 분포한 지역