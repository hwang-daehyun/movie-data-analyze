# **groupby**
#- 같은 값을 한 그룹으로 묶어서 여러 가지 연산 및 통계를 구할 수 있습니다.
#- `데이터.groupby(컬럼명).연산및통계함수`


import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

df['PassengerId'] = df['PassengerId'].astype(str)

## **단일 그룹**
#count()|행의 갯수|
print(df.groupby('Pclass').count())

#nunique()|행의 유니크한 갯수|
print(df.groupby('Pclass').nunique()) #유니크한 갯수

#sum()|합|
print(df.groupby('Pclass').sum(numeric_only=True))

#mean()|평균|
print(df.groupby('Pclass').mean(numeric_only=True))

#min()|최솟값|
print(df.groupby('Pclass').min(numeric_only=True))

#max()|최댓값|
print(df.groupby('Pclass').max(numeric_only=True))

#std()|표준편차|
print(df.groupby('Pclass').std(numeric_only=True))

#var()|분산|
print(df.groupby('Pclass').var(numeric_only=True))

print(df.groupby('Pclass')[['Survived']].mean())
print(df.groupby('Pclass')[['Survived','Age']].mean())


## **다중 그룹**
print(df.groupby(['Sex','Pclass']).mean(numeric_only=True))

import numpy as np

df.groupby(['Sex','Pclass'])[['Survived','Age','SibSp','Parch','Fare']].aggregate([np.mean, np.min, np.max])