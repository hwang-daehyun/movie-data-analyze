# **plotly로 유형별 그래프 그리기**

## **[1] 산점도**

'''
px.scatter(data_frame=데이터, x=X축 컬럼, y=Y축 컬럼, color=색, trendline='ols') #trendline은 추세선 추가
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


penguins = sns.load_dataset('penguins')

print(penguins)

fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', color='sex', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

# 스타일 변경 symbol=
fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', color='island', symbol='sex', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

# 그래프를 나눠서 보고자 할때 facet_col = 나눌 변수 
fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', color='sex', facet_col='island', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', trendline='ols', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.scatter(data_frame=penguins, x='bill_length_mm', y='bill_depth_mm', color='sex', facet_col='island', trendline='ols', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()


## **[2] 분포 살펴보기**
'''
px.histogram(data_frame=데이터, x=X축 컬럼, color=색) #히스토그램
px.box(data_frame=데이터, x=X축 컬럼, y=Y축 컬럼, color=색) #상자그림
'''

### **히스토그램**
fig = px.histogram(data_frame=penguins, x='flipper_length_mm', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

## **상자그림**
fig = px.box(data_frame=penguins, x='body_mass_g', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.box(data_frame=penguins, x='body_mass_g', y='species', color='sex', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()


## **[3] 막대 그래프**
'''
px.bar(data_frame=데이터, x=X축 컬럼, y=Y축 컬럼, color=색, barmode='group') #쌓아서 올리지 않으면 barmode = 'group'을 추가한다
'''

titanic = sns.load_dataset('titanic')
print(titanic)


titanic_groupby = titanic.groupby(['sex','class'])[['survived']].mean().reset_index()
print(titanic_groupby)


fig = px.bar(data_frame=titanic_groupby, x='class', y='survived', color='sex', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.bar(data_frame=titanic_groupby, x='class', y='survived', color='sex', barmode='group', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

# text_auto='.2f'를 사용시 바의 수치가 바로 써져서 보임.2f라 소수점 2자리
fig = px.bar(data_frame=titanic_groupby, x='class', y='survived', color='sex', barmode='group', text_auto='.2f', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

titanic_groupby1 = titanic.groupby(['sex','class','alone'])[['survived']].mean().reset_index()
print(titanic_groupby1)


fig = px.bar(data_frame=titanic_groupby1, x='class', y='survived', color='sex', facet_col='alone', barmode='group', text_auto='.2f', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()



## **[4] 선그래프**
'''
px.line(data_frame=데이터, x=X축 컬럼, y=Y축 컬럼, color=색)
'''


flights = sns.load_dataset("flights")
print(flights)

may_flights = flights.query('month == "May"')
fig = px.line(data_frame=may_flights, x="year", y="passengers", color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

fig = px.line(data_frame=flights, x="year", y="passengers", color='month', color_discrete_sequence=px.colors.qualitative.Set2, template='plotly_white')
fig.show()

## **[5] 히트맵**
'''
px.imshow(데이터, text_auto=텍스트포맷, color_continuous_scale=컬러맵)
'''

titanic_corr = titanic[['survived','age','fare','sibsp','pclass']].corr()
print(titanic_corr)

fig = px.imshow(titanic_corr, text_auto='.2f', color_continuous_scale='YlOrBr')
fig.show()

titanic_pivot = pd.pivot_table(data=titanic, index='sex', columns='class', values='survived', aggfunc='mean')
print(titanic_pivot)

fig = px.imshow(titanic_pivot, text_auto='.2f', color_continuous_scale='Purples')
fig.show()


## **[6] 파이차트**
'''
px.pie(data_frame=데이터, values=값, names=라벨)
'''

df = px.data.tips()
print(df)

fig = px.pie(df, values='tip', names='day', color_discrete_sequence=px.colors.qualitative.Pastel)
fig.show()

df.groupby('day')[['tip']].sum()
