import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

#- `isna()`: 결측값을 True로 반환합니다.


print(df.info())
print(df.isna())
print(df.isna().sum())
print(df[df['Age'].isna()])
print(df[df['Embarked'].isna()])

#- `notna()`: 결측값을 False로 반환합니다.
print(df.notna())
print(df.notna().sum())
print(df[df['Age'].notna()])
print(df[df['Embarked'].notna()])

## **[2] 결측값 제거**
#`데이터명.dropna(axis=0, how='any', subset=None)`

#- axis : {0: index / 1: columns}
#- how : {'any' : 존재하면 제거 / 'all' : 모두 결측치면 제거}
#- subset : 행/열의 이름을 지정합니다.

print(df.dropna())  # 결측지가 없는 데이터 출력
print(df.dropna(axis=1))  # 결측지가 있는 행이 삭제
print(df.dropna(how='any')) # 결측지가 없는 데이터 출력
print(df.dropna(subset=['Cabin','Age'])) # 특정 열에 결측지가 없는 데이터 출력


## **[3] 결측값 대치**
#- 데이터 전체의 결측값을 특정 값으로 변경
#    - `데이터명.fillna(대치할값)`
#- 특정 컬럼의 결측값을 특정 값으로 변경
#    - `데이터명[컬럼명].fillna(대치할값)`
#- 결측값을 바로 위의 값과 동일하게 변경
#    - `데이터명.fillna(method='ffill')`
#- 결측값을 바로 아래의 값과 동일하게 변경
#    - `데이터명.fillna(method='bfill')`

print(df.tail())
print(df.fillna(-1).tail())

df1 = df.copy()
df1['Age'] = df1['Age'].fillna(-1)
print(df1.tail())

df1 = df.copy()
df1['Age'] = df1['Age'].fillna(round((df1['Age'].mean())))  #특정 변수의 데이터의 평균값으로 결측지를 채워줌
print(df1.tail())

print(df.fillna(method='ffill').tail())
print(df.fillna(method='bfill').tail())