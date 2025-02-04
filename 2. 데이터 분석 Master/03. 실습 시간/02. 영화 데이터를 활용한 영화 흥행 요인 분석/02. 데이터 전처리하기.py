import pandas as pd
import numpy as np

## **질문 만들기**
#- 연도별 흥행 수익은?
#- 가장 흥행한 영화 TOP 10은?
#- 흥행에 가장 성공한 감독과 배우는?
#- 장르와 흥행 수익
    #- 흥행 수익이 좋은 장르는?
    #- 시간의 흐름에 따라 유행하는 장르가 바뀌는가?
    #- 월별로 흥행하는 장르가 있는가?
#- 수익과 예산, 투표수, 평점과의 상관관계는?
#- ROI(예산 대비 수익)가 높으면서 흥행에 성공한 영화의 특징은?
#- 개봉일과 흥행 수익


movies = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습2_ 영화 데이터를 활용한 영화 흥행 요인 분석\\tmdb_5000_movies.csv")
'''print(movies.head(5))
print(movies.columns)'''

credits = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습2_ 영화 데이터를 활용한 영화 흥행 요인 분석\\tmdb_5000_credits.csv")
'''print(credits.head(5))
print(credits.columns)'''

movies_df = movies[['id', 'budget', 'genres', 'title', 'release_date', 'revenue', 'vote_average', 'vote_count']]
credits_df = credits[['movie_id', 'crew', 'cast']]

# 열삭제 axis = 1 
data = pd.merge(movies_df, credits_df, left_on= 'id', right_on= 'movie_id').drop('movie_id', axis = 1)
'''print(data.head(5))'''

# ROI 컬럼 만들기

#- budget: 영화 예산 (단위: 달러)
#- revenue: 흥행 수익 (단위: 달러)
data['roi'] = data['revenue'] / data['budget']
'''print(data.head(5))'''


# 감독 컬럼 만들기
'''print(data['crew'][[0]])'''
# 문자열로 되어 있는 파이썬 자료형을 파이썬 자료형으로 바꾸는 라이브러리
import ast
'''print(ast.literal_eval(data['crew'][0]))'''
data['crew'] = data['crew'].apply(ast.literal_eval)

# 감독 이름만 뽑아오기
def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']

data['director'] = data['crew'].apply(get_director)
'''print(data['director'])'''


# 배우 컬럼 만들기
'''print(data['cast'][0])'''
data['cast_name'] = data['cast'].apply(lambda x: [i['name'] for i in ast.literal_eval(x)])
'''print(data.head(5))'''

# 장르 컬럼 만들기
data['genres'] = data['genres'].apply(ast.literal_eval)

def get_genres(x):
    if len(x) > 0:
        return x[0]['name']

data['main_genres'] = data['genres'].apply(get_genres)
'''print(data.head(5))'''

# 데이터 타입 변경
'''print(data.info())'''

data['release_date'] = pd.to_datetime(data['release_date'], format='%Y-%m-%d')
data['id'] = data['id'].astype(str)

'''print(data.info())'''

# 연도, 월 컬럼 만들기
data['year'] = data['release_date'].dt.year
data['month'] = data['release_date'].dt.month
'''print(data.info())'''

# 결측기 제거
data.dropna(inplace=True)
'''print(data.info())'''

print(data.head(5))

