import pandas as pd

data = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\Part3) 파이썬 데이터 분석 실습\\Data\\실습5_ 교통 데이터를 활용한 지리 데이터 시각화\\서울시 지하철 호선별 역별 시간대별 승하차 인원 정보.csv", encoding = 'cp949')
'''print(data.head())'''

#- 서울시 지하철 승하차인원의 월별 합계
#- 2018년 이후, 2호선만, 승차 인원만 분석 예정

## **질문 만들기**
#- 승차 인원이 가장 많은 역은?
#- 연도별로 혹은 월별로 승차 인원 추이에 차이가 있는가?
#- 시간대별로 가장 승차인원이 많은 역은?
#- 지하철역 시간대별 인원 유형 군집화
#- 지도에 분석 결과를 시각화하기

## **데이터 전처리**

#- 날짜 컬럼 추가
data['연도'] = pd.to_datetime(data['사용월'], format='%Y%m').dt.year
data['월'] = pd.to_datetime(data['사용월'], format='%Y%m').dt.month

'''print(data.head())'''

#- 2018년 이후, 2호선만 필터링
data = data.query('연도 >= 2018').query('호선명 == "2호선"')
data = data.query('호선명 == "2호선" and 연도 >= 2018')
'''print(data)'''


#- 지하철역명 통일
'''print(sorted(data['지하철역'].unique()))'''
data['지하철역'] = [i[0] for i in data['지하철역'].str.split('(')]
'''print(sorted(data['지하철역'].unique()))'''

#- 승차 인원만 추출하기
on_col = [i for i in data.columns if '승차' in i]
data = data[['사용월', '연도','월','지하철역']+on_col]
print(data.head())