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