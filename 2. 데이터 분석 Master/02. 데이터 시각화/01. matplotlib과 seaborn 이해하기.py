# **matplotlib과 seaborn 이해하기**

#- **`matplotlib`**: 파이썬 데이터 시각화의 가장 기본적인 라이브러리. 유연하게 커스텀이 가능하나 코드가 길고 어렵다는 단점이 있습니다.
#- **`seaborn`**: **`matplotlib`**을 좀 더 쉽고 아름답게 시각화하는 라이브러리
#- 실제 분석에서는 **`seaborn`**과 **`matplotlib`**을 함께 사용하여 시각화하는 경우가 많습니다.

## **[1] 기본 문법**

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

#plt.figure(figsize=(가로길이, 세로길이)) #그래프 크기 설정
#sns.000plot(data=데이터, x=X축 컬럼, y=Y축 컬럼, hue=범례 컬럼) #seaborn으로 그래프 그리기
#plt.title(제목) #제목 설정
#plt.xlabel(라벨) #x축 라벨 설정
#plt.ylabel(라벨) #y축 라벨 설정
#plt.legend(loc=범례 위치 설정)
#plt.xticks(rotation=x축 각도 설정)
#plt.yticks(rotation=y축 각도 설정)
#plt.show() #그래프 출력

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('penguins')


'''plt.figure(figsize=(10,5))
sns.barplot(data=df, x='species', y='body_mass_g')
plt.title('body mass per spcies')
plt.xlabel('per species')
plt.ylabel('body mass')
plt.show()

sns.barplot(data=df, x='island', y='body_mass_g', hue='sex')
plt.show()

sns.barplot(data=df, x='island', y='body_mass_g', hue='sex')
plt.xticks(rotation=30)
plt.legend(loc='upper left')
plt.show()'''

## **[2] 스타일 설정하기**

#sns.set_style(스타일) -> 배경색이나 형태
#sns.set_palette(팔레트) -> 그래프의 색상
#- 스타일: darkgrid, whitegrid, dark, white -> grid : 값별 선을 그어서 보여줌.
#- 팔레트: [참고](https://seaborn.pydata.org/tutorial/color_palettes.html)

'''sns.set_style('darkgrid')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_style('whitegrid')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_style('white')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_style('dark')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_palette('Set3')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_style('white')
sns.set_palette('flare')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()

sns.set_palette('crest')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.show()'''

## **[3] 한글 폰트 설정**

# 코랩 기준 #
#1.   폰트 설치
#!sudo apt-get install -y fonts-nanum
#!sudo fc-cache -fv
#!rm ~/.cache/matplotlib -rf

#2.   런타임 다시 시작
#3.   폰트 적용

#plt.rc('font', family='NanumGothic')

#한글 폰트 미적용시
sns.barplot(data=df, x='species', y='body_mass_g')
plt.title('펭귄의 종별 몸무게')
plt.show()

plt.rc("font", family = "Malgun Gothic")
#unicode minus를 사용하지 않기 위한 설정 (minus 깨짐현상 방지)
sns.set(font="Malgun Gothic", rc={"axes.unicode_minus":False}, style='white')
sns.barplot(data=df, x='species', y='body_mass_g')
plt.title('펭귄의 종별 몸무게')
plt.show()


## **[4] 고화질 설정**

#%config InlineBackend.figure_format = 'retina'

#%config InlineBackend.figure_format = 'retina'
sns.barplot(data=df, x='species', y='body_mass_g')
plt.title('펭귄의 종별 몸무게')
plt.show()