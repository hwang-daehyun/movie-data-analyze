import pandas as pd

#- 두 개의 데이터를 특정 컬럼을 기준으로 합칩니다.
#- 결합 방법에는 4가지가 있습니다.
#- `pd.merge(데이터1, 데이터2, on=기준컬럼, how=결합방법)`



customer = pd.DataFrame({'id' : [i for i in range(1,7)],
                    'name' : ['민준','서연','서준','도현','지윤','채원'],
                    'age' : [15,30,40,20,23,31]})
print(customer)

orders = pd.DataFrame({'id' : [1,1,2,3,3,4,5,7,7,7],
                    'item' : ['사과','체리','바나나','사과','바나나','바나나','체리','사과','체리','바나나'],
                    'quantity' : [1, 2, 1, 1, 3, 2, 2, 3, 2, 1]})
print(orders)


print(pd.merge(customer, orders, on='id', how='inner'))

print(pd.merge(customer, orders, on='id', how='left'))

print(pd.merge(customer, orders, on='id', how='right'))

print(pd.merge(orders, customer, on='id', how='left'))

print( pd.merge(customer, orders, on='id', how='outer'))


#- 두 데이터의 기준 컬럼명이 다를 경우에는
#    - `pd.merge(데이터1, 데이터2, left_on=데이터1의 기준컬럼, right_on=데이터2의 기준컬럼, how=결합방법)`


orders = orders.rename({'id':'customer_id'}, axis=1)


print(pd.merge(customer, orders, left_on='id', right_on='customer_id', how='inner'))