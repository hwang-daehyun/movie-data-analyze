import pandas as pd


file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)



## **apply 함수**
#- 사용자 정의 함수를 데이터에 적용하고 싶을 때 사용합니다.
#- `.apply(함수, axis=0/1)`

df1 = df.copy()

def pclass_sibsp(x):
    if x['Pclass'] == 1 and x['SibSp'] == 1:
        return 1
    else:
        return 0
    
df1['pclass_sibsp_filter'] = df1.apply(pclass_sibsp, axis=1)

print(df1.head())

import numpy as np

def adult(x):
    if x >= 19:
        return 1
    elif x < 19:
        return 0
    else:
        return np.nan
    
df1['adult_yn'] = df1['Age'].apply(adult)
print(df1.head(10))

df1['pclass_sibsp_lambda'] = df1.apply(lambda x: 1 if x['Pclass'] == 1 and x['SibSp'] == 1 else 0, axis=1)
print(df1.head())

## **map 함수**
#- 값을 특정 값으로 치환하고 싶을 때 사용합니다.
#- `데이터명[컬럼명].map(매핑 딕셔너리)`

gender_map = {'male':'남자', 'female':'여자'}
df1['Sex_kr'] = df1['Sex'].map(gender_map)
print(df1.head())

## **문자열 다루기**
#|메소드|설명|
#|:--|:--|
#|`.str.contains(문자열)`|문자열을 포함하고 있는지 유무|
#|`.str.replace(기존문자열, 대치문자열)`|문자열 대치|
#|`.str.split(문자열, expand=True/False, n=개수)`|특정 문자열을 기준으로 쪼개기|
#|`.str.lower()`|소문자로 바꾸기|
#|`.str.upper()`|대문자로 바꾸기|

df2 = df.copy()
print(df.head())

# .str.contains(문자열)

df['Name'].str.contains('Mrs')
df2[df2['Name'].str.contains('Mrs')]

# .str.replace(기존문자열, 대채문자열)

df2['Name'] = df2['Name'].str.replace(',', '')
print(df2.head())

# .str.split(문자열, expand=True/False, n=개수)
print(df2['Name'].str.split(' '))
print(df2['Name'].str.split(' ', expand=True, n=1))
