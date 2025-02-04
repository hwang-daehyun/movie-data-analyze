import pandas as pd

file_path = "C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv"

df = pd.read_csv(file_path)


## **stack, unstack**
# - stack : 컬럼 레벨에서 인덱스 레벨로 데이터프레임을 변경합니다.
# - unstack : 인덱스 레벨에서 컬럼 레벨로 데이터프레임을 변경합니다.
#  - stack의 반대입니다.

pivot = pd.pivot_table(df, index=['Sex','Pclass'], values=['Survived','Fare'], aggfunc=['mean','median','sum'])
print(pivot)

print(pivot.stack(0)) #컬럼의 첫번째 레벨을 인덱스로 내립니다.

print(pivot.stack(1)) #컬럼의 두번째 레벨을 인덱스로 내립니다.

print(pivot.unstack(0)) #인덱스의 첫번째 레벨을 컬럼으로 쌓아 올립니다

print(pivot.unstack(1)) #인덱스의 두번째 레벨을 컬럼으로 쌓아 올립니다

## **melt**
#- `pd.melt(데이터명, id_vars=기준 컬럼)`

data = pd.DataFrame({'name':['a','b','c']
                    , 'order_count':[3,4,10]
                    , 'amount':[10000,25000,300000]})

print(data)

print(pd.melt(data, id_vars=['name']))

#var_name / value_name으로 이름을 변경할 수 있다.
print(pd.melt(data, id_vars=['name'], var_name='type', value_name='val'))