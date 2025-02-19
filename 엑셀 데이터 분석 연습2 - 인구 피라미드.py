# 1. 인구 피라미드
import pandas as pd
import matplotlib.pyplot as plt


## 2011년 데이터 
# 남자 데이터 정의
df_m = pd.read_excel('C:\\Users\\dhwhang\\Downloads\\201102_201102_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,E:Y')   # skiprows을 쓸 경우 3번째 줄까지 스킵하고 데이터를 불러옴/ usecols는 특정 변수들만 불러올수 있다.
# 숫자로 바꿔주는 작업
df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int)
print(df_m)


# 여자 데이터 정의
df_w = pd.read_excel('C:\\Users\\dhwhang\\Downloads\\201102_201102_연령별인구현황_월간.xlsx', skiprows=3, index_col='행정기관', usecols='B,AB:AV')   # skiprows을 쓸 경우 3번째 줄까지 스킵하고 데이터를 불러옴/ usecols는 특정 변수들만 불러올수 있다.
df_w.columns=df_m.columns #컬럼명 통일
# 숫자로 바꿔주는 작업
df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int)
print(df_w)

# 시각화 시키기
import matplotlib
plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, -df_m.iloc[0]//1000) #단위 : 천 명
plt.barh(df_w.columns, df_w.iloc[0]//1000) #단위 : 천 명
plt.title('2011 대한민국 인구 피라미드')
plt.savefig('2011_인구피라미드.jpg', dpi=100)
plt.show()


## 2024년 데이터

# 남자 데이터 정의
df_m = pd.read_excel('C:\\Users\\dhwhang\\Downloads\\201102_201102_연령별인구현황_월간 (1).xlsx', skiprows=3, index_col='행정기관', usecols='B,E:Y')   # skiprows을 쓸 경우 3번째 줄까지 스킵하고 데이터를 불러옴/ usecols는 특정 변수들만 불러올수 있다.
# 숫자로 바꿔주는 작업
df_m.iloc[0] = df_m.iloc[0].str.replace(',','').astype(int)
print(df_m)


# 여자 데이터 정의
df_w = pd.read_excel('C:\\Users\\dhwhang\\Downloads\\201102_201102_연령별인구현황_월간 (1).xlsx', skiprows=3, index_col='행정기관', usecols='B,AB:AV')   # skiprows을 쓸 경우 3번째 줄까지 스킵하고 데이터를 불러옴/ usecols는 특정 변수들만 불러올수 있다.
df_w.columns=df_m.columns #컬럼명 통일
# 숫자로 바꿔주는 작업
df_w.iloc[0] = df_w.iloc[0].str.replace(',','').astype(int)
print(df_w)

# 시각화 시키기
import matplotlib
plt.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 #글자 크기
matplotlib.rcParams['axes.unicode_minus'] = False 

plt.figure(figsize=(10,7))
plt.barh(df_m.columns, -df_m.iloc[0]//1000) #단위 : 천 명
plt.barh(df_w.columns, df_w.iloc[0]//1000) #단위 : 천 명
plt.title('2024 대한민국 인구 피라미드')
plt.savefig('2024_인구피라미드.jpg', dpi=100)
plt.show()