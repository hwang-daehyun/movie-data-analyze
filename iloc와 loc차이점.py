import pandas as pd


data = [[0,1,2,3],
        [4,5,6,7],
        [8,9,10,11],
        [12,13,14,15]]

df = pd.DataFrame(data)

indexing_boolean = [True, False, True, False]

# print(df.loc[indexing_boolean])
# print(df.iloc[indexing_boolean])

#.loc는 눈에 보이는 인덱스 라벨명을 사용
#.iloc는 행들의 위치 값을(인자로) 받는다.

df=df.rename(index={0:2, 1:3, 2:1, 3:0})

print(df.loc[[0, 2]])
print('*'*15)
print(df.iloc[[0, 2]])
print('*'*15)
print(df.iloc[[0, 2, 3],[2,3]])


#Apply는 함수에 있는거 사용하는거 

