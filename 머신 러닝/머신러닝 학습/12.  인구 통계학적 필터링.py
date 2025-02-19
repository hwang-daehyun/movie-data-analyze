## 영화 추천 시스템

# 1. Demographic Filtering (인구통계학적 필터링)
# 2. Content Based Filtering (컨텐츠 기반 필터링)
# 3. Collaborative Filtering (협업 필터링)


## 1. Demographic Filtering (인구통계학적 필터링)
import pandas as pd
import numpy as np

df1 = pd.read_csv("C:\\Users\\User\\Desktop\\tmdb_5000_credits.csv")
df2 = pd.read_csv("C:\\Users\\User\\Desktop\\tmdb_5000_movies.csv")

# df1과 df2 데이터 합치기
'''print(df1['title'].equals(df2['title']))'''
'''print(df1.columns)'''  # 컬럼 변경을 위해 한번 실행
df1.columns = ['id', 'title', 'cast', 'crew']
df1[['id', 'cast', 'crew']]
df2 = df2.merge(df1[['id', 'cast', 'crew']], on='id')

# 영화의 평점이 10/10 -> 5명이 평가
# 영화의 평점이 8/10  -> 500명이 평가

C = df2['vote_average'].mean()
m = df2['vote_count'].quantile(0.9)   # 영화평가수의 하위 90퍼센트만 뽑는 것
'''print(m)'''  # 결과 1838.4000000000015 결국 상위 10퍼에 해당하는 평가수의 기준은 1838.4라는 얘기이다.


q_movies = df2.copy().loc[df2['vote_count'] >= m]
'''print(q_movies)'''
q_movies['vote_count'].sort_values()

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)


q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score', ascending=False)

'''print(q_movies[['title', 'vote_average', 'vote_count','score']])'''

pop= df2.sort_values('popularity', ascending=False)

import matplotlib.pyplot as plt

'''plt.figure(figsize=(12,4))

plt.barh(pop['title'].head(10),pop['popularity'].head(10), align='center',
        color='skyblue')
plt.gca().invert_yaxis()
plt.xlabel("Popularity")
plt.title("Popular Movies")
plt.show()
'''

## 2. Content Based Filtering (줄거리 - 컨텐츠 기반 필터링)
'''print(df2['overview'].head())'''

# 텍스트 분석을 위해 백터화 해야된다.
# Bag of Words - BOW
# 1. TfidfVectorizer (TF-IDF 기반의 백터화)
# 2. CountVectorizer

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')

'''from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
print(ENGLISH_STOP_WORDS)'''

'''print(df2['overview'].isnull().values.any())'''  # overview에 대한 null값 확인

df2['overview'] = df2['overview'].fillna(' ')

tfidf_matrix = tfidf.fit_transform(df2['overview'])

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
'''print(cosine_sim)'''

indices = pd.Series(df2.index, index = df2['title']).drop_duplicates()  # 영화 제목을 넣으면 인덱스 값을 반환해주는 것을 만듬

# 영화의 제목을 입력받으면 코사인 유사도를 통해서 가장 유사도가 높은 상위 10개의 영화 목록 반환
def get_recommendation(title, cosine_sim=cosine_sim):
    # 영화 제목을 통해서 영화의 전체데이터 중 인덱스 값을 반환해주는 것을 만듬
    idx = indices[title]
    # 코사인 유사도 [cosine_sim]에서 idx에 해당하는 데이터를 [idx, 유사도] 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key = lambda x: x[1], reverse=True)
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    # 인덱스 정보를 통해 영화 제목을 추출
    return df2['title'].iloc[movie_indices]

'''print(df2['title'].head())
print(get_recommendation('The Dark Knight Rises'))'''


## 2. Content Based Filtering (감독,장르,키워드 등 - 컨텐츠 기반 필터링)

# 장르에서 보면 형태가 str로 들어가 있음. 이걸 리스트 형태로 바꾸기 위해서
# from ast import literal_eval 을 실행하여 바꿔야 한다.

from ast import literal_eval
features = ['cast', 'crew', 'keywords', 'genres']

for feature in features:
    df2[feature] = df2[feature].apply(literal_eval)

'''print(df2.loc[0, 'crew'])'''

# 감독 정보를 추출하는 함수
def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

df2['director'] = df2['crew'].apply(get_director)
'''print(df2['director'])
print(df2[df2['director'].isnull()])'''

# 처음 3개의 데이터 중에서 name 에 해당하는 value 만 추출
def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        if len(names) > 3:
            names = names[:3]
        return names
    return []

features = ['cast', 'keywords', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(get_list)

'''print(df2[['title', 'cast', 'director', 'keywords', 'genres']].head())'''

def clean_data(x):
    if isinstance(x,list):
        return [str.lower(i.replace(' ','')) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(' ',''))
        else:
            return ''
        
features = ['cast', 'keywords', 'genres', 'director']
for feature in features:
    df2[feature] = df2[feature].apply(clean_data)

'''print(df2[['title', 'cast', 'director', 'keywords', 'genres']].head())'''

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
df2['soup'] = df2.apply(create_soup, axis=1)

'''print(df2[['title', 'soup']].head())'''


from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])
'''print(count_matrix.shape)'''

from sklearn.metrics.pairwise import cosine_similarity
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
'''print(cosine_sim2)'''

df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])

'''print(get_recommendation('The Avengers', cosine_sim2))'''

import pickle

movies = df2[['id', 'title']].copy()

pickle.dump(movies, open('movies.pickle', 'wb'))
pickle.dump(cosine_sim2, open('cosine_sim2.pickle', 'wb'))