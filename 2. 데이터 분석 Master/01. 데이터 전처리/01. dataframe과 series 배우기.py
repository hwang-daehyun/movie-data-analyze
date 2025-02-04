import pandas as pd


# Series 이해하기

# 딕셔너리 시리즈
'''
dic = {'a' : 1, 'b' : 2, 'c' : 3}
dic_series = pd.Series(dic)
print(dic)
print(dic_series)
'''
# 리스트 시리즈
'''
ls = [1, 2, 3]
ls_series = pd.Series(ls, index=['a', 'b', 'c'])
print(ls)
print(ls_series)'''

# 시리즈의 값, 인덱스, 값의 타입 확인하기
'''
print(dic_series.values, end='\n\n')
print(dic_series.index, end='\n\n')
print(dic_series.dtype, end='\n\n')

print(ls_series.values, end='\n\n')
print(ls_series.index, end='\n\n')
print(ls_series.dtype, end='\n\n')'''


# Dataframe 이해하기

# 딕셔너리로 데이터 프레임 만들기
'''
dic = {'Name' : ['John', 'Merry', 'Cheis'],
       'Number' : [1, 2, 3],
       'Month' : ['Feb', 'Oct', 'Nov']}

dic_Dataframe = pd.DataFrame(dic)

print(dic)
print(dic_Dataframe)'''


# 리스트로 데이터 프레임 만들기
'''
ls = [['John', 1, 'Feb'],
      ['Merry', 2, 'Oct'],
      ['Cheis', 3, 'Nov']]

ls_Dataframe = pd.DataFrame(ls, columns=['Name', 'Number', 'Month'], index = range(1,4))

print(ls)
print(ls_Dataframe)
'''

# 시리즈로 데이터 프레임 만들기
'''
name_series = pd.Series(['John', 'Merry', 'Chris'])
number_series = pd.Series([1,2,3])
month_series = pd.Series(['Feb', 'Oct', 'Nov'])
df = pd.DataFrame({'Name' : name_series, 'Number' : number_series, 'Month' : month_series})

print(df)'''

# 데이터프래임의 값, 인덱스, 값의 타입, 컬럼 알아보기
'''
print(df.values, end='\n\n')
print(df.index, end='\n\n')
print(df.dtypes, end='\n\n')
print(df.columns)'''


# 데이터 프레임 살펴보기

import pandas as pd

file_path = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part2) 파이썬을 이용한 데이터 분석\\data\\titanic_train.csv")

data = file_path

print(data.head())
print(data.tail())
print(data.info())
print(data.dtypes)
print(data.describe())