# apply & applymap은 series 및 Dataframe의 각 요소에 함수 적용할 때 사용

import pandas as pd

sr = pd.Series([1, 2, 3, 4, 5])

result = sr.apply(lambda x: x**2)
'''print(result)'''

# apply는 Series와 DataFrame에서 사용 가능

data = {'학교' : ['A고', 'B고', 'C고','D고'],
        '학생 수(특수)' : ['1000(10)', '250(0)', '400(0)', '600(2)']}

df = pd.DataFrame(data)
'''print(df)'''



df['학생 수'] = df['학생 수(특수)'].apply(lambda x: int(x.split('(')[0]))

def assign_grade(student_num):
    if student_num >= 1000:
        return 'Big_Num'
    elif student_num >= 500:
        return 'Mid_Num'
    else:
        return 'Row_Num'
df['학생 수 등급'] = df['학생 수'].apply(assign_grade)    


# lambda (인자): (표현식1) if (조건식) else (표현식2)

df['학생 수 등급(추가)'] = df['학생 수'].apply(lambda x: 'Big_Num' if x >= 1000 else 'Row_Num') 


print(df)


# applymap은 DataFrame의 모든 요소에 함수를 적용할 때 사용.
df =  pd.DataFrame({'A' : [1, -2, 3],
                    'B' : [4, 5, -6],
                    'C' : [-7, 8, 9]})

result_def = df.map(abs)
'''print(result_def)'''

result_def = df.map(lambda X:X*2)
'''print(result_def)'''

# 내장 함수 사용하는 apply
df = pd.DataFrame({'A' : [1, 2, 3, 4],
                   'B' : [5, 6, 7, 8]})
'''print(df)'''

sum_df = df.apply(sum, axis=0)
'''print(sum_df)'''

# 사용자 함수 사용하는 apply
df =  pd.DataFrame({'학년' : [1, 2, 3, 4],
                    '반' : [1, 5, 2, 6],
                    '이름' : ['한수아', '최건우', '이재은', '김송이']})
print(df)
def make_nameplate(row):
    return f"{row['학년']}학년 {row['반']}반 {row['이름']}"

df['명찰'] = df.apply(make_nameplate, axis=1)
print(df)

# lambda 함수 사용하는 apply
df['명찰2'] = df.apply(lambda row: f"{row['학년']}학년 {row['반']}반 {row['이름']}", axis=1)
print(df)