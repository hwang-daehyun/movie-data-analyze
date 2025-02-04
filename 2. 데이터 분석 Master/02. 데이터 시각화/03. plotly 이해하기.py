#**`plotly`**는 인터랙티브한 그래프를 그릴 수 있는 라이브러리입니다.
#인터랙티브한 그래프를 html로 저장하기 용이합니다.

## **[1] 기본 문법**

'''fig = px.그래프종류(data_frame=데이터, x=X축 컬럼, y=Y축 컬럼, color=범례 컬럼, title=제목,
                 labels=dict(X축 컬럼=X축 라벨, Y축 컬럼=Y축 라벨),
                 width=그래프 가로길이, height=그래프 세로길이, text_auto=True/False)
fig.show()
'''


import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
print(df)

df_groupby = df.groupby('species')[['body_mass_g']].mean().reset_index()
print(df_groupby)

sns.barplot(data=df_groupby, x='species', y='body_mass_g')

fig = px.bar(df_groupby, x='species', y='body_mass_g')
fig.show()

df_groupby1 = df.groupby(['island','sex'])[['body_mass_g']].mean().reset_index()
print(df_groupby1)

sns.barplot(data=df_groupby1, x="island", y="body_mass_g", hue="sex")
plt.show()

fig = px.bar(data_frame=df_groupby1, x='island', y='body_mass_g', color='sex')
fig.show()

fig = px.bar(data_frame=df_groupby1, x='island', y='body_mass_g', color='sex', barmode='group', text_auto='.0d', width=700, height=500, title='island별 몸무게 평균', labels=dict(body_mass_g='몸무게(g)', island='', sex='성별'))
fig.show()

## **[2] 스타일 설정하기**
'''
template=템플릿명
color_discrete_sequence = 컬러맵명 #범주형 데이터
color_continuous_scale= 컬러맵명 #연속형 데이터
'''

# - 템플릿 적용
for temp in ['ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white', 'plotly_dark']:
    fig = px.bar(data_frame=df_groupby1, x='island', y='body_mass_g', color='sex', barmode='group', text_auto='.0d', width=700, height=500, title=f'템플릿: {temp}', labels=dict(body_mass_g='몸무게(g)', island='', sex='성별'), template=temp)
    fig.show()



# - 컬러맵 적용
fig = px.colors.sequential.swatches_continuous()
fig.show()

fig = px.colors.qualitative.swatches()
fig.show()

for color_map in [px.colors.qualitative.Pastel1, px.colors.qualitative.Safe, px.colors.qualitative.Antique]:
    fig = px.bar(data_frame=df_groupby1, x='sex', y='body_mass_g', color='island', barmode='group', text_auto='.0d', width=700, height=500, color_discrete_sequence=color_map)
    fig.show()


for color_map in [px.colors.sequential.Burg, px.colors.sequential.Mint, px.colors.sequential.PuBuGn]:
    fig = px.scatter(data_frame=df, x='bill_length_mm', y='bill_depth_mm', color='flipper_length_mm', width=700, height=500, color_continuous_scale=color_map, template='simple_white')
    fig.show()

## **[3] HTML 파일로 저장하기**

'''
fig.write_html(파일경로 및 파일명)
'''

fig = px.scatter(data_frame=df, x='bill_length_mm', y='bill_depth_mm', color='flipper_length_mm', width=700, height=500, color_continuous_scale=px.colors.sequential.PuBuGn, template='plotly_white')
fig.show()
fig.write_html('test.html')



