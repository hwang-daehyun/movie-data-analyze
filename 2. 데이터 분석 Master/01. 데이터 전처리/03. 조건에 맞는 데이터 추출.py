import pandas as pd


file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

### **기본적인 방법**
# - 행
# - 한 개
#    - `데이터프레임명[인덱스:인덱스+1]`
# - 여러 개
#    - `데이터프레임명[시작인덱스:끝인덱스+1]`

df = pd.read_csv(file_path)

'''print(df[3:6])'''


#- 열
# - 한 개
#    - `데이터프레임[컬럼명]`
#    - `데이터프레임.컬럼명`
# - 여러 개
#    - `데이터프레임[[컬럼명1, 컬럼명2, ...]]`

'''
print(df['Survived'])
print(df.Survived)
print(df['Survived'].to_frame)  # 데이터 프레임 형태로 데이터를 불러오는 방법 1.
print(df[['Survived']])     # 데이터 프레임 형태로 데이터를 불러오는 방법 2.
print(df[['Survived', 'Pclass']])'''

#- loc: 레이블값을 사용하여 조회   -> 즉, 인덱스 값을 활용하여 추출하는 거다
# -> 그렇기 때문에 만약 set_index를 통해 인덱스를 이름으로 바꾸면 이름을 찾아 사용해야함
# EX] df1.loc['Heikkinen, Miss. Laina',]
# - `데이터프레임명.loc[행조건,열조건]`
# - 열만 조회할때는 행조건에 `:`를 입력합니다.

'''
print(df.loc[3,])
print(df.loc[:,'Name'])
print(df.loc[3,'Name'])
print(df.loc[3:5,])
print(df.loc[3:5,['Age','Name']])
print(df.loc[[1,3,5],['Age','Name']])  #특정 인덱스의 값만 갖고 오고 싶을때 행에 리스트로 인덱스 값을 넣기'''


#- iloc: 위치인덱스를 사용하여 조회 -> 즉, 인덱스가 어떤거라도 위치로 불러오기 때문에 더 편함.
# - `데이터프레임명.iloc[행인덱스조건,열인덱스조건]`

'''
print(df.iloc[3,])
print(df.iloc[3:5,])
print(df.iloc[3:7,2:4])'''


### **데이터 정렬하기**
#- `데이터프레임명.sort_values(정렬기준컬럼)`
#- 내림차순으로 정렬하고 싶다면 `ascending=False` 조건을 걸어주면 됩니다.

'''
print(df.head())
print(df.sort_values('Age'))
print(df.sort_values('Age', ascending=False))
print(df.sort_values(['Age','Fare'], ascending=[False,True]))'''


### **특정 조건을 충족하는 데이터 추출하기**
#- `데이터프레임명[조건식]`
#- `데이터프레임명.query('조건식')`

'''print(df[df['Pclass'] == 1])
print(df[(df['Pclass'] == 1) & (df['Age'] >= 30)])
print(df[(df['Pclass'] == 1) | (df['Age'] >= 30)])
print(df.query('Pclass == 1'))
print(df.query('Pclass == 1 and Age >= 30'))
print(df.query('Pclass == 1 or Age >= 30'))
print(df[df['PassengerId'].isin([3,100,500])])
print(df.query('PassengerId in [3,100,500]'))
print(df.query('PassengerId.isin([3,100,500])'))
'''
import random

passengerid_list = list(df['PassengerId'])

# random.sample 함수를 사용하여 리스트에서 10개의 숫자를 무작위로 선택
passengerid_sample = random.sample(passengerid_list, 10)

print(df[df['PassengerId'].isin(passengerid_sample)])


# @ 기호는 query 문법 내에서 함수 외부 변수를 참조할 때 사용함.
print(df.query('PassengerId in @passengerid_sample'))