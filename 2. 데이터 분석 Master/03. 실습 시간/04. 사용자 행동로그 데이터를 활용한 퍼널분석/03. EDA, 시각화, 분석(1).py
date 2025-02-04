import pandas as pd
import plotly.express as px

data = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습4_ 사용자 행동 로그 데이터를 활용한 퍼널 분석\\ecommerce_behavior.csv")

data.drop('Unnamed: 0', axis=1 ,inplace=True)

## **데이터 전처리**

#Index(['Unnamed: 0', 'event_time', 'event_type', 'product_id', 'category_id',
#       'category_code', 'brand', 'price', 'user_id', 'user_session'],

# -데이터 타입 변경
data['event_time'] = pd.to_datetime(data['event_time'], format='%Y-%m-%d %H:%M:%S UTC')

#category_code, brand에 너무 많은 컬럼이 비어있고, 카테고리나 브랜드별로 분석할 계획이 없으므로 해당 컬럼을 제거한다.
data.drop(['category_code', 'brand'], axis=1, inplace=True)

# -날짜 컬럼 추가
data['date_ymd'] = data['event_time'].dt.date
data['date_ymd'] = pd.to_datetime(data['date_ymd'], format='%Y-%m-%d')


## **분석**

### [1] DAU(일간 활성 사용자수) 추이는?
#- 어느 요일에 가장 많이 방문하는가?
dau = data.groupby('date_ymd')[['user_id']].nunique().reset_index().rename({'user_id':'dau'}, axis=1)
'''print(dau)'''
fig = px.line(data_frame=dau, x='date_ymd', y='dau', title='DAU 추이')
'''fig.show()'''

dau['day_of_week'] = dau['date_ymd'].dt.day_name()
dau['day_of_week1'] = dau['date_ymd'].dt.day_of_week
'''print(dau.head())'''

avg_dau_dow = dau.groupby(['day_of_week', 'day_of_week1'])[['dau']].mean().reset_index()
avg_dau_dow.sort_values('day_of_week1', inplace=True)
'''print(avg_dau_dow)'''
fig = px.bar(data_frame=avg_dau_dow, x='day_of_week', y='dau', title='요일별 DAU 평균', width=700, height=500)
'''fig.show()'''


### [2] 사이트 체류시간 평균은?
#- 조회만 한 유저, 카트에 담은 유저, 구매까지 한 유저별로 체류시간이 어떻게 다른가?

#- 한 세션의 끝에서 시작 시간을 뺀 값을 체류시간으로 정의한다.
data.query('user_session == "2806ff10-08bc-4811-9ab7-af074fe22a88"').sort_values('event_time')

duration = data.groupby('user_session')[['event_time']].agg(['max','min']).reset_index()
duration['duration'] = duration['event_time']['max'] - duration['event_time']['min']
duration.columns = ['user_session', 'max', 'min', 'duration']
'''print(duration)'''

#- 체류시간 평균 구하기
duration['duration'].mean()

#- 조회만 한 유저, 카트에 담은 유저, 구매까지 한 유저별로 체류시간이 어떻게 다른가?
session_pivot = pd.pivot_table(data=data, index='user_session', columns='event_type', values='event_time', aggfunc='count').reset_index().fillna(0)
'''print(session_pivot)'''
cart_session = list(session_pivot.query('cart > 0')['user_session'])
purchase_session = list(session_pivot.query('purchase > 0')['user_session'])

view_session_avg_duration = duration.query('user_session not in @cart_session and user_session not in @purchase_session')['duration'].mean()
cart_session_avg_duration = duration.query('user_session in @cart_session')['duration'].mean()
purchase_session_avg_duration = duration.query('user_session in @purchase_session')['duration'].mean()

print(f'조회만 한 유저의 평균 체류시간: {view_session_avg_duration}')
print(f'카트에 담은 유저의 평균 체류시간: {cart_session_avg_duration}')
print(f'구매까지 한 유저의 평균 체류시간: {purchase_session_avg_duration}')