import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

## **[1] 타입 확인**
#- `.dtypes`는 열의 타입을 시리즈로 반환합니다.

print(df.dtypes)

#- 특정 타입을 가진 컬럼만 추출
#    - `데이터명.select_dtypes(타입)`

print(df.select_dtypes('int'))
print(df.select_dtypes('object'))


## **[2] 타입 변환**
#`데이터명[컬럼명].astype(타입)`

print(df['PassengerId'])

print(df['PassengerId'].astype(str))

df1 = df.copy()
df1['PassengerId'] = df1['PassengerId'].astype(str)
print(df1.info())

print(df['Age'])

'''df['Age'].astype(int)'''
# ->  에러 나는 이유는 Age 변수 안에 nan 데이터가 있기 때문에 그렇다

print(df['Age'].fillna(-1).astype(int))

df1 = df.copy()
df1['Age'] = df1['Age'].fillna(-1).astype(int)
print(df1.tail())


import numpy as np

df1 = df.copy()
df1['Age'] = df1['Age'].fillna(-1).astype(int).replace(-1, np.nan)
# -> nan 값을 그대로 살리고 싶다면, 먼저 숫자형으로 변환 후 rapalce로 -1분에는 numpy함수를 사용하여
# nan으로 교체 해줘야 한다.

print(df1.tail())