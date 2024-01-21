import pickle
import streamlit as st # 웹페이지 제작
from tmdbv3api import Movie, TMDb

NUMEXPR_MAX_THREADS=4

movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'db0c86430fe777976ba1dabefe3826bb'
tmdb.language = 'ko-KR' # 데이터가 한국 기준

def get_recommendations(title): # 주피터노트북 코드 활용
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값을 얻기
    idx = movies[movies['title'] == title].index[0]

    # 코사인 유사도 매트릭스 (cosine_sim) 에서 idx 에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim_scores = list(enumerate(cosine_sim[idx]))

    # 코사인 유사도 기준으로 내림차순 정렬
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim_scores = sim_scores[1:11]
    
    # 추천 영화 목록 10개의 인덱스 정보 추출
    movie_indices = [i[0] for i in sim_scores]
    
    # 인덱스 정보를 통해 영화 제목 추출
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        # detail 정보: https://developer.themoviedb.org/reference/movie-details
        image_path = details['poster_path']
        if image_path: # 참고: https://developer.themoviedb.org/reference/collection-images
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else: #영화의 이미지 정보가 없을 수도 있음.
            image_path = 'no_image.jpg'

        images.append(image_path)
        titles.append(details['title'])

    return images, titles
    
movies = pickle.load(open('movies.pickle', 'rb')) # movies.pickle를 가져옴
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb')) # cosine_sim.pickle를 가져옴

st.set_page_config(layout='wide')
st.header('Soonflix')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like', movie_list)

if st.button('Recommend'):
    with st.spinner('Please wait...'): # 자료가 나올때까지 기다리는 Progress Bar
        images, titles = get_recommendations(title)

        idx = 0
        for i in range(0, 2): #2줄
            cols = st.columns(5) #5개
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1