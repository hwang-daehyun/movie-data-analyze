import pandas as pd
import plotly.express as px

data = pd.read_csv("C:\\Users\\dhwhang\\Desktop\\쉽게 배우는 파이썬 데이터 분석\\패스트 캠퍼스\\drive-download-20240910T020903Z-001\\Data\\실습4_ 사용자 행동 로그 데이터를 활용한 퍼널 분석\\ecommerce_behavior.csv")

data.drop('Unnamed: 0', axis=1 ,inplace=True)

## **데이터 전처리**
'''print(data.info())
'''
#Index(['Unnamed: 0', 'event_time', 'event_type', 'product_id', 'category_id',
#       'category_code', 'brand', 'price', 'user_id', 'user_session'],

# -데이터 타입 변경
data['event_time'] = pd.to_datetime(data['event_time'], format='%Y-%m-%d %H:%M:%S UTC')
'''print(data.head())
print(data.info())'''

'''print(data.isna().sum())'''

#category_code, brand에 너무 많은 컬럼이 비어있고, 카테고리나 브랜드별로 분석할 계획이 없으므로 해당 컬럼을 제거한다.
data.drop(['category_code', 'brand'], axis=1, inplace=True)
'''print(data.head())'''

# -날짜 컬럼 추가
data['date_ymd'] = data['event_time'].dt.date
'''print(data.info())'''
data['date_ymd'] = pd.to_datetime(data['date_ymd'], format='%Y-%m-%d')
print(data.info())