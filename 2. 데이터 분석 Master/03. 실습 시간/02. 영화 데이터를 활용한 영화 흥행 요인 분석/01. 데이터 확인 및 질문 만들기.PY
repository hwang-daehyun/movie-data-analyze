import pandas as pd

movies = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습2_ 영화 데이터를 활용한 영화 흥행 요인 분석\\tmdb_5000_movies.csv")
print(movies.head(5))

movies = pd.read_csv("C:\\Users\\User\\Desktop\\패스트 캠퍼스 데이터 마스터\\파이썬\\Part3) 파이썬 데이터 분석 실습\\Data\\실습2_ 영화 데이터를 활용한 영화 흥행 요인 분석\\tmdb_5000_credits.csv")
print(movies.head(5))

#**movies 데이터**
#- budget: 영화 예산 (단위: 달러)
#- genres: 모든 장르
#- homepage: 공식 홈페이지
#- id: 각 영화당 unique id
#- original_language: 원 언어
#- original_title: 원 제목
#- overview: 간략한 설명
#- popularity: TMDB에서 제공하는 인기도
#- production_companies: 모든 제작사
#- production_countries: 모든 제각국가
#- release_date: 개봉일
#- revenue: 흥행 수익 (단위: 달러)
#- runtime: 상영 시간
#- spoken_language: 사용된 모든 언어
#- status: 개봉 여부
#- title: 영문 제목
#- vote_avearage: TMDB에서 받은 평점 평균
#- vote_count: TMDB에서 받은 투표수

#**credits 데이터**
#- movie_id: 각 영화당 unique id
#- title: 영문 제목
#- cast: 모든 출연진
#- crew: 모든 제작진

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
