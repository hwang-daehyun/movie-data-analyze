import pandas as pd

df = {}
df1 = {}
df2 = {}

count_series = df['학생 수'] >= 500
# 결과 -> True / False 값으로 나옴


selected_data = df[df['학생 수'] >= 500]
# 결과 -> 조건의 True값의 해당하는 데이터만 출력

# 여러 가지 조건으로 사용할 경우
selected_data = df[(df['학생 수'] >= 500) & (df['남녀공학'] == '남녀공학')]
selected_data = df[(df['학생 수'] >= 500) | (df['남녀공학'] == '남녀공학')]
# ~ 부정의미
selected_data = df[~(df['학생 수'] >= 500)]



# accessor
data = {'학교' : ['A고', 'B고', 'C고', 'D고'],
        '지역' : ['서울특별시 강남구', '서울특별시 용산구', '서울특별시 강남구', '성남시 분당구']}

df = pd.DataFrame(data)

# 지역 값 중 시작이 '서울'인 데이터만 찾기
selected_data = df[df['지역'].str.startswith('서울')]
# 지역 값중 '강남'이 들어간 데이터만 찾기
selected_data = df[df['지역'].str.contains('강남')]
#isin 같은 경우 series 매소드라 str을 사용 안해도 됨
selected_data = df[df['지역'].isin(['서울특별시 강남구', '성남시 분당구'])]


#Concat
df_concat = pd.concat([df1, df2], ignore_index=True)
# ignore_index=True -> 기존 인덱스를 무시하고 전체 인덱스를 0부터 시작

# 그냥 추가
df_concat['추가 컬럼'] = pd.Series(['추가1', '추가2', '추가3'])

# concat으로 추가
# axis=0 세로 방향 / axis=1 가로 방향
df_concat_column = pd.Series(['추가1', '추가2', '추가3'], name='추가 컬럼')
df_concat = pd.concat([df1, df_concat_column], axis=1)


