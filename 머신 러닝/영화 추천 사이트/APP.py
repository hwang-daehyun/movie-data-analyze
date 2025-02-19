# 집에서 할때 아래 패키지 깔고 하기
# pip install streamlit
# pip install tmdbv3api
import pickle 
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'ff7106dccbd04732ca14138eb3ddc87f'
tmdb.language = 'ko-KR'

def get_recommendation(title):
     # 영화 제목을 통해서 영화의 전체데이터 중 인덱스 값을 반환해주는 것을 만듬
    idx = movies['title' == title].index[0]
    # 코사인 유사도 [cosine_sim]에서 idx에 해당하는 데이터를 [idx, 유사도] 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))
    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores,key=lambda x:x[1], reverse=True)
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    # 인덱스 정보를 통해 영화 제목을 추출
    images = []
    titles = []
    for i in movie_indices:
        movies['id'].iloc[i]
        details = movie.details(id)

        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'


        images.append('https://image.tmdb.org/t/p/w500' + details['poster_path'])
        titles.append(details['title'])
    return images, titles

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim2.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('Deaflix')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like', movie_list)
if st.button('Recommend'):
    with st.spinner('Please wait>>>'):
        imges, title = get_recommendation(title)

        idx = 0
        for i in range(0,2):
            cols = st.columns(5)
            for col in cols:
                col.image(imges[idx])
                col.write(title[idx])
                idx += 1



