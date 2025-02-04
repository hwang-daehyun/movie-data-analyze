import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\temperatures.csv"

data = pd.read_csv(file_path)

df = data.copy()


## **문자형을 날짜형으로 변경**
#- 날짜가 문자형으로 되어있다면 날짜형으로 변경해야 여러가지 날짜 계산을 할 수 있습니다.
#- `pd.to_datetime(컬럼, format='날짜 형식')`

#|형식|설명|
#|:--|:--|
#|%Y|0을 채운 4자리 연도|
#|%y|0을 채운 2자리 연도|
#|%m|0을 채운 월|
#|%d|0을 채운 일|
#|%H|0을 채운 시간|
#|%M|0을 채운 분|
#|%S|0을 채운 초|

pd.to_datetime(df['Date'], format='%Y-%m-%d')

df['Date1'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
print(df.info())

print(df.head())

## **날짜를 원하는 형식으로 변경**
#`데이터컬럼.dt.strftime(날짜형식)`

print(df['Date1'].dt.strftime('%Y-%m'))

print(df['Date1'].dt.strftime('%m-%d %H:%M'))

## **dt 연산자**
#|연산자|설명|
#|:--|:--|
#|year|연도|
#|month|월|
#|day|일|
#|dayofweek|요일(0-월요일, 6-일요일)|
#|day_name()|요일을 문자열로|


df['year'] = df['Date1'].dt.year
df['month'] = df['Date1'].dt.month
df['day'] = df['Date1'].dt.day
df['dayofweek'] = df['Date1'].dt.dayofweek
df['dayname'] = df['Date1'].dt.day_name()

print(df.head())

## **날짜 계산**
#- day 연산: `pd.Timedelta(day=숫자)` -> 일자만 계산 가능
#- month 연산: `DateOffset(months=숫자)`
#- year 연산: `DateOffset(years=숫자)`

df['plus day1'] = df['Date1'] + pd.Timedelta(days=1)
print(df.head())

df['plus day7'] = df['Date1'] + pd.Timedelta(days=7)
print(df.head())

df['minus day7'] = df['Date1'] - pd.Timedelta(days=7)
print(df.head())

from pandas.tseries.offsets import DateOffset

df['plus month1'] = df['Date1'] + DateOffset(months=1)
print(df.head())

df['minus month3'] = df['Date1'] - DateOffset(months=3)
print(df.head())

df['plus year1'] = df['Date1'] + DateOffset(years=1)
print(df.head())

df['minus year3'] = df['Date1'] - DateOffset(years=3)
print(df.head())


## **날짜 구간 데이터 만들기**
#`pd.date_range(start=시작일자, end=종료일자, periods=기간수, freq=주기)`

#|형식|설명|
#|:--|:--|
#|D|일별|
#|W|주별|
#|M|월별 말일|
#|MS|월별 시작일|
#|A|연도별 말일|
#|AS|연도별 시작일|

pd.date_range(start='2020-01-01', periods=30, freq='D')

pd.date_range(start='2020-01-01', end='2023-06-30', freq='M')

pd.date_range(start='2020-01-01', end='2023-06-30', freq='MS')

pd.date_range(start='2020-01-01', end='2023-06-30', freq='A')

pd.date_range(start='2020-01-01', end='2023-06-30', freq='AS')

## **기간 이동 계산**
#`컬럼.rolling().집계함수`

df1 = data.copy()
df1.head()

#7일 이동평균
df1['ma7'] = df1['Temp'].rolling(7).mean()
print(df1.head(20))

df1['ma30'] = df1['Temp'].rolling(30).mean()
print(df1.head(30))

#- 평균 외에 합계, 최솟값, 최댓값 등 다양한 연산이 가능합니다.

print(df1['Temp'].rolling(7).sum())

print(df1['Temp'].rolling(7).min())

print(df1['Temp'].rolling(7).max())

## **행 이동**
#`컬럼.shift(이동할 행의 수)`

df2 = data.copy()

df2['Temp shift1'] = df2['Temp'].shift(1)
print(df2.head())

df2['pct change'] = (df2['Temp shift1'] - df2['Temp'])/df2['Temp']
print(df2.head())

print(df2['Temp'].shift(7).head(10))

print(df2['Temp'].shift(-1).head(10))