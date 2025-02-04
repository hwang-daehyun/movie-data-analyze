## **[1] 산점도**


# sns.scatterplot(data=데이터, x=X축 컬럼, y=Y축 컬럼, hue=색) #산점도 기본
# sns.lmplot(data=데이터, x=X축 컬럼, y=Y축 컬럼, hue=색) #산점도에 회귀선 추가

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

sns.set_palette('Set2')

#%config InlineBackend.figure_format = 'retina'

print(penguins)

sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm')
plt.show()

sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex')
plt.show()

sns.scatterplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', style='sex', hue='island')
plt.show()

# 구역을 나눠서 표를 보고 싶다면 relplot을 통해 하며, col='island'을 통해 island에 따라 나눌 수 있다.
sns.relplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex', col='island', kind='scatter')
plt.show()

sns.lmplot(data=penguins, x='bill_length_mm', y='bill_depth_mm')
plt.show()

sns.lmplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex', col='island')
plt.show()

## **[2] 분포 살펴보기**


# sns.displot(data=데이터, x=X축 컬럼, hue=색) #히스토그램
# sns.displot(data=데이터, x=X축 컬럼, hue=색, kind='kde') #밀도 분포
# sns.boxplot(data=데이터, x=X축 컬럼, y=Y축 컬럼, hue=색) # 상자 그림
# sns.pairplot(data=데이터, hue=색) #여러 컬럼들간의 분포

### **히스토그램**

sns.displot(data=penguins, x='flipper_length_mm')
plt.show()

sns.displot(data=penguins, x='flipper_length_mm', kde=True)
plt.show()

### **밀도 분포**

sns.displot(data=penguins, x="flipper_length_mm", kind="kde")
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", hue='species', kind="kde")
plt.show()

sns.displot(data=penguins, x="flipper_length_mm", hue='species', col='sex', kind="kde")
plt.show()

sns.boxplot(data=penguins, x='body_mass_g')
plt.show()

sns.displot(data=penguins, x='body_mass_g', kde=True)
plt.show()

sns.boxplot(data=penguins, x='body_mass_g', y='species', hue='sex')
plt.show()

sns.pairplot(data=penguins)
plt.show()

sns.pairplot(data=penguins, hue='species')
plt.show()


## **[3] 막대 그래프**

# sns.countplot(data=데이터, x=X축 컬럼, hue=색) #X축의 범주별로 행의 개수를 카운트하여 시각화
# sns.barplot(data=데이터, y=Y축 컬럼, hue=색) #막대그래프


titanic = sns.load_dataset('titanic')
print(titanic)

sns.countplot(data=titanic, x='class', hue='alive')
plt.show()

sns.countplot(data=titanic, x='sex', hue='alive')
plt.show()

sns.barplot(data=titanic, x='class', y='survived', hue='sex')
plt.show()



## **[4] 선그래프**

# sns.lineplot(data=데이터, x=X축 컬럼, y=Y축 컬럼, hue=색)

flights = sns.load_dataset("flights")
print(flights)

may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
plt.show()


sns.lineplot(data=flights, x="year", y="passengers", hue='month')
plt.show()


# **[5] 히트맵**

# sns.heatmap(data=데이터, annot=값 표시 여부, fmt=값 포맷(서수점), cmap=컬러맵)

print(titanic.head())

titanic_corr = titanic[['survived','age','fare','sibsp','pclass']].corr()

sns.heatmap(data=titanic_corr, annot=True, fmt='.2f', cmap='YlOrBr')
plt.show()

titanic_pivot = pd.pivot_table(data=titanic, index='sex', columns='class', values='survived', aggfunc='mean')
print(titanic_pivot)

sns.heatmap(data=titanic_pivot, annot=True, fmt='.2f', cmap='Purples')
plt.show()





