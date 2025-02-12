# 리스트 컴프리헨션
#[expressin for item in iterable if condition]
# expressin -> item을 어떻게 담아줄지를 하는 것

# 노가다
a=[1,4,9,16,25,36,49,64,81,100]

# 일반적인 for문
'''squares = []
for i in range(1, 11):
    squares.append(i*i)

print(squares)'''


# 리스트 컴프리헨션
'''squares_1 = [i*i for i in range(1, 11)]
print(squares_1)'''

# 특정 조건만 새로운 리스트로 만들기
'''my_list = ['apple', 'banana', 'cat', 'dog', 'elephant']

new_list=[]
for i in my_list:
    if 'e' in i:
        new_list.append(i)

print(new_list)

new_list1 = [i for i in my_list if 'e' in i]
print(new_list1)'''




import pandas as pd

df = pd.DataFrame({'이름': ['황대현', '이솔예', '황영민', '황서현', '박현자'],
                   '나이': [23, 24, 25, 26, 32],
                   '직업': ['전사', '마법사', '격투가', '힐러', '탱커']})


print(df)


df['연령'] = [i+10 for i in df['나이']]
print(df)  

df_2= df[['이름','나이']]


print(df_2)

for i,j in zip(df['이름'], df['나이']):
    print(i,   j)
'''
황대현 23
이솔예 24
황영민 25
황서현 26
박현자 32'''


for i,j in df_2.iterrows():
    print(i,j)
'''
0 이름    황대현
나이     23
Name: 0, dtype: object
1 이름    이솔예
나이     24
Name: 1, dtype: object
2 이름    황영민
나이     25
Name: 2, dtype: object
3 이름    황서현
나이     26
Name: 3, dtype: object
4 이름    박현자
나이     32
Name: 4, dtype: object'''



for i,j in df_2.items():
    print(i,j)
'''
이름 0    황대현
1    이솔예
2    황영민
3    황서현
4    박현자
Name: 이름, dtype: object
나이 0    23
1    24
2    25
3    26
4    32
Name: 나이, dtype: int64'''


for i in df_2.items():
    print(i)
'''
'이름', 0    황대현
1    이솔예
2    황영민
3    황서현
4    박현자
Name: 이름, dtype: object)
('나이', 0    23
1    24
2    25
3    26
4    32
Name: 나이, dtype: int64)'''