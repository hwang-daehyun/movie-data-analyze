import pandas as pd

data = [1, 2, 3, 4, 5]
print(data)
# 출력 결과 -> [1, 2, 3, 4, 5]

series = pd.Series(data)
print(series)
# 출력 결과 
'''
0    1
1    2
2    3
3    4
4    5'''



data = [1, 2, 3, 4, 5]
series = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print(series['B'])
print(series['D'])
print(series[1:4])
print(series['B':'D'])


# 열 : 데이터 속성(세로)
# 행 : 개별 데이터 항목(가로)

# DataFrame 생성 방법

# 방법 1
data = [
    {'이름': '철수', '나이': 25, '성별': '남'},
    {'이름': '영희', '나이': 22, '성별': '여'},
    {'이름': '민수', '나이': 30, '성별': '남'},
    {'이름': '지영', '나이': 28, '성별': '여'},
    {'이름': '세희', '나이': 27, '성별': '여'},
    {'이름': '동수', '나이': 26, '성별': '남'},
    {'이름': '민지', '나이': 29, '성별': '여'},
]

df = pd.DataFrame(data)

# 방법 2
data = {
    '이름': ['철수', '영희', '민수', '지영', '세희', '동수', '민지'],
    '나이': [25, 22, 30, 28, 27, 26, 29],
    '성별': ['남', '여', '남', '여', '여', '남', '여'],
}

df = pd.DataFrame(data)

# 방법 3
data = [
    ['철수', 25, '남'],
    ['영희', 22, '여'],
    ['민수', 30, '남'],
    ['지영', 28, '여'],
    ['세희', 27, '여'],
    ['동수', 26, '남'],
    ['민지', 29, '여'],
]

df = pd.DataFrame(data, columns=['이름', '나이', '성별'],
                  index=['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# loc
# loc 속성과 인덱스 값을 이용해 전체 데이터 중 일부를 선택할 수 있습니다.
print(df.loc['A':'E', '이름':'나이'])

# iloc
# loc 속성과 정수 위치를 이용해 전체 데이터 중 일부를 선택할 수 있습니다.
print(df.iloc[0:5, :2])