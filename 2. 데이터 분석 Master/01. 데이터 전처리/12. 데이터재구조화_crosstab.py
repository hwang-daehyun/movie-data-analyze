import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

# **crosstab**
#- 범주형 데이터를 비교분석할 때 유용합니다.
# - `pd.crosstab(index=행, columns=열, margins=True/False, normalize=True/False)` margins : 행의 합 / normalize : 비율


## **범주별 갯수 구하기**
#- `pd.crosstab(행, 열)`

print(pd.crosstab(df['Sex'], df['Survived']))
print(pd.crosstab(df['Pclass'], df['Survived']))

## **범주별 비율 구하기**
#- `normalize = 'all'`: 전체 합이 100%
#- `normalize = 'index'`: 행별 합이 100%
#- `normalize = 'columns'`: 열별 합이 100%

print(pd.crosstab(df['Sex'], df['Survived'], normalize='all'))

print(pd.crosstab(df['Sex'], df['Survived'], normalize='index'))

print(pd.crosstab(df['Sex'], df['Survived'], normalize='columns'))

print(pd.crosstab(df['Sex'], df['Survived'], normalize='all', margins=True))

print(pd.crosstab(df['Sex'], df['Survived'], normalize='index', margins=True))

print(pd.crosstab(df['Sex'], df['Survived'], normalize='columns', margins=True))

## **다중 인덱스, 다중 컬럼의 범주표 구하기**

print(pd.crosstab(index=[df['Sex'], df['Pclass']], columns=df['Survived']))

print(pd.crosstab(index=[df['Sex'], df['Pclass']], columns=df['Survived'], normalize='all'))

print(pd.crosstab(index=[df['Sex'], df['Pclass']], columns=df['Survived'], normalize='columns'))

print(pd.crosstab(index=[df['Sex'], df['Pclass']], columns=[df['Survived'], df['Embarked']]))

print(pd.crosstab(index=[df['Sex'], df['Pclass']], columns=[df['Survived'], df['Embarked']], normalize='all'))