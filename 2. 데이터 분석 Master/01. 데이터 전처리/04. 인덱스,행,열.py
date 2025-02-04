import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)

df.index


'''print(list(df.index))'''


### **인덱스 변경**
#- 인덱스 몇개를 바꿀 때
#    - `데이터명.rename({인덱스:바꿀 인덱스, 인덱스:바꿀 인덱스, ...})`
#- 인덱스 전체를 바꿀 때
#    - `데이터명.index = 바꿀 인덱스 리스트`


df1 = df.copy()
'''df1.rename({0:'row1', 1:'row2'})

print(df1.head())''' #rename은 데이터프레임을 바꾸어주지 않으므로 변경을 하려면 다시 덧씌워주어야 합니다.

'''df1 = df1.rename({0:'row1', 1:'row2'})
print(df1.head())

df1.index = [i+1 for i in range(len(df1))]
print(df1.head())
'''

### **열을 인덱스로 설정**
# - `데이터명.set_index(컬럼명)`
'''
df1.set_index('PassengerId')
print(df1.head())'''

'''df1 = df1.set_index('PassengerId') #마찬가지로 변경을 하려면 덧씌워주어야 합니다.
print(df1.head())'''

### **인덱스를 열로 변환**
#- 인덱스를 열로 변환하고 그 열을 남기고 싶으면
#    - `데이터명.reset_index()`
#- 인덱스를 열로 변환하고 그 열을 삭제하고 싶으면
#    - `데이터명.reset_index(drop = True)`

'''df1.reset_index()
df1.reset_index(drop=True)
df1 = df1.reset_index()
print(df1.head())'''


### **행의 추가/제거**
#- 행의 추가
#    - `pd.concat([기존 데이터명, 붙일 데이터명])`
#- 행의 제거
#    - `데이터명.drop(인덱스명, axis=0)`

df1 = df.copy()
df2 = df.copy()

'''print(df1)
print(df2)'''

'''df3 = pd.concat([df1, df2])
print(df3)
'''
'''df3 = df3.reset_index(drop=True)
print(df3)

df3.drop([i for i in range(891, len(df3))])
print(df3)'''


### 행 중복 제거
#- `데이터명.drop_duplicates()`

'''df3.drop_duplicates()
print(df3)'''


### **열의 추가/제거**

#- 열의 추가
#    - `데이터명[추가할 컬럼명] = 추가할 값`
#- 열의 제거
#    - `데이터명.drop(제거할 컬럼명, axis=1)`
'''df1 = df.copy()
df1['age_simplified'] = df1['Age']//10 * 10

print(df1['age_simplified'])

print(list(df1['Name'].str.split(',')))''' #문자열 컬럼에 str.split()을 쓰면 특정 문자열을 기준으로 자를 수 있습니다.

'''df1['given_name'] = [i[0] for i in df1['Name'].str.split(',')]
print(df1.head())

df1['string_add'] = df1['Sex']+df1['given_name']
print(df1.head())

df1['number_add'] = df1['Age'] + df1['age_simplified']
print(df1.head())

df1.drop('given_name', axis=1)
print(df1.head())'''


### **열 이름 변경**
#- 열 이름 하나를 바꿀 때
#    - `데이터명.rename({열이름:바꿀이름, 열이름:바꿀이름, ...}, axis=1)`
#- 열 이름 전체를 바꿀 때
#    - `데이터명.columns = 열 이름 리스트`

df1 = df.copy()

df1.rename({'PassengerId':'Id'}, axis=1)

df1.columns = [i for i in range(12)]
print(df1.head())