import pandas as pd
import numpy as np

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
'''print(data.head(5))'''


## **분석**
import plotly.express as px

### [1] 연도별 흥행 수익은?

# reset_index()를 하는 이유는  year로 그룹 바이를 했기때문에 인덱스로 들어가 인덱스를 초기화 시켜주는 거임.
revenue_by_year = data.groupby('year')[['revenue']].sum().reset_index()
'''print(revenue_by_year)'''
fig = px.line(data_frame=revenue_by_year, x="year", y="revenue")
'''fig.show()'''
# -> 2000년대에 들어 급격히 흥행 수익이 높아졌다.


### [2] 가장 흥행한 영화 TOP 10은?
top =  data.groupby('title')[['revenue']].sum().reset_index()
'''print(top)'''
'''fig = px.bar(data_frame = top, x = 'title', y = 'revenue', title=f'흥행 수익 TOP 10 영화')
fig.show()'''# -> 이렇게 하면 뒤죽박죽으로 나옴 내 생각에 솔트 후 head(10)으로 해서 데이터 저장 후 하는게 좋을 듯

# -> 이렇게 수정하여 진행할 수도 있음
top = top.sort_values('revenue', ascending=False).sort_values('revenue').head(10)
fig = px.bar(data_frame = top, x = 'title', y = 'revenue', title=f'흥행 수익 TOP 10 영화')
'''fig.show()'''
'''top_10 = top.sort_values('revenue', ascending=False)[:10]
fig = px.bar(data_frame = top_10, x = 'title', y = 'revenue', title=f'흥행 수익 TOP 10 영화')
fig.show()'''

# 예산 TOP 10, 투표수 TOP 10 영화는?
title_dic = {'budget' : '예산', 'vote_count' : '투표수'}
for y in ['budget', 'vote_count']:
    top = data.groupby('title')[[y]].sum().reset_index().sort_values(y, ascending=False).head(10)
    fig = px.bar(data_frame=top, x='title', y=y, title = f"{title_dic[y]} TOP 10 영화")
'''    fig.show()'''

# -> 대체적으로 예산, 투표수가 높으면 흥행 수익도 높아보이나, 정비례하진 않아 보인다. -> 상관관계 분석을 진행필요

### [3] 흥행에 가장 성공한 감독과 배우는?
#- 가장 수익이 많은 감독, 배우는?
top_director = data.groupby(['director'])['revenue'].sum().reset_index().sort_values('revenue', ascending=False).head(10)
fig = px.bar(data_frame=top_director, x='director', y='revenue', title=f"흥행 수익 TOP 10 감독")
'''fig.show()'''

revenue_cast = data[['revenue', 'cast_name']].explode('cast_name')

top_cast = revenue_cast.groupby('cast_name')[['revenue']].sum().reset_index().sort_values('revenue', ascending=False).head(10)
fig = px.bar(data_frame=top_cast, x='cast_name', y='revenue', title=f"흥행 수익 TOP 10 배우")
'''fig.show()'''
# -> 유명 감독과 배우 일부가 많은 흥행 수익을 차지하고 있다.

### [4] 장르와 흥행 수익
#- 흥행 수익이 좋은 장르는?
#- 시간의 흐름에 따라 유행하는 장르가 바뀌는가?
#- 월별로 흥행하는 장르가 있는가?

#- 장르별 흥행 수익 분포
fig = px.box(data_frame = data, y = 'main_genres', x = 'revenue', hover_name = 'title')
'''fig.show()'''

# -> 액션과 드라마 장르에 흥행 수익이 아주 높은 영화들이 많이 있지만, 중앙값을 비교하면 다른 장르에 비해 높은 편은 아니다.
genre_avg_revenue = data.groupby('main_genres')[['revenue']].mean().reset_index()
fig = px.bar(data_frame = genre_avg_revenue, x = 'main_genres', y = 'revenue', title = '장르별 흥행 수익 평균')
'''fig.show()'''

# -> 장르별 영화 수익 평균은 애니메이션 > 어드벤쳐 > 가족 > SF > 판타지 > 액션 순이다.

genre_sum_revenue = data.groupby('main_genres')[['revenue']].sum().reset_index()
fig = px.bar(data_frame = genre_sum_revenue, x = 'main_genres', y = 'revenue', title = '장르별 흥행 수익 합계')
'''fig.show()'''

# -> 장르별 영화 수익 합계는 액션 > 어드벤쳐 > 드라마 > 코  미디 > 애니메이션 > 액션 순이다.

#- 연도별 장르별 수익
revenue_by_year_genre = data.query('year >= 1990').groupby(['year', 'main_genres'])[['revenue']].sum().reset_index()
fig = px.bar(data_frame = revenue_by_year_genre, x='year', y='revenue', color='main_genres', color_continuous_scale=px.colors.qualitative.Light24_r)
'''fig.show()'''


revenue_by_year_genre_pct = pd.pivot_table(data=data.query('year >= 1990'), index='year', columns='main_genres', values='revenue', aggfunc=sum, fill_value=0, margins=True)
revenue_by_year_genre_pct = 100 * revenue_by_year_genre_pct.div(revenue_by_year_genre_pct.iloc[:,-1], axis=0).drop('All').drop('All', axis=1)
# melt -> 행열 바꾸기
revenue_by_year_genre_pct = pd.melt(revenue_by_year_genre_pct.reset_index(), id_vars='year', value_name='pct')
fig = px.bar(data_frame=revenue_by_year_genre_pct, x="year", y="pct", color='main_genres', color_discrete_sequence=px.colors.qualitative.Light24_r)
'''fig.show()'''
 
# -> 2010년도부터 액션 영화의 흥행 수익 비중이 높아지기 시작했다.
# -> 1990년대 후반 ~ 2000년대 초반에는 드라마 장르의 흥행 수익이 높았다.


revenue_by_month_genre = data.query('year >= 1990').groupby(['month','main_genres'])[['revenue']].sum().reset_index()
fig = px.bar(data_frame=revenue_by_month_genre, x="month", y="revenue", color='main_genres', color_discrete_sequence=px.colors.qualitative.Light24_r)
'''fig.show()'''

revenue_by_month_genre_pct = pd.pivot_table(data=data.query('year >= 1990'), index='month', columns='main_genres', values='revenue', aggfunc=sum, fill_value=0, margins=True)
revenue_by_month_genre_pct = 100 * revenue_by_month_genre_pct.div(revenue_by_month_genre_pct.iloc[:,-1], axis=0).drop('All').drop('All', axis=1)
revenue_by_month_genre_pct = pd.melt(revenue_by_month_genre_pct.reset_index(), id_vars='month', value_name='pct')

fig = px.bar(data_frame=revenue_by_month_genre_pct, x="month", y="pct", color='main_genres', color_discrete_sequence=px.colors.qualitative.Light24_r)
fig.show()

# -> 액션, 어드벤처 장르는 비교적 봄, 여름에 개봉 수익이 높았다.
# -> 드라마 장르는 비교적 가을, 겨울에 개봉 수익이 높았다.
# -> 코미디 장르는 비교적 겨울에 개봉 수익이 높았다.