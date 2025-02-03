import numpy as np
import streamlit as st
import pickle
import os
import requests
# Load the model
working_dir = os.path.dirname(os.path.abspath(__file__)) 
movies_list = pickle.load(open(f'{working_dir}/movies_list.sav','rb'))
similarity = pickle.load(open(f'{working_dir}/similarity.sav','rb'))

movies = movies_list

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=e959f4d39cbd62730180bf9fda9737fc&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

st.header("Movie Recommender System")
select_value = st.selectbox("Select The Movie: ",movies['title'].values)

import streamlit.components.v1 as components

imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/frontend/public")

imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
   
    ]


imageCarouselComponent(imageUrls=imageUrls, height=200)

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[0:10]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations "):
  movie_name, movie_poster = recommend(select_value)
  col1,col2,col3,col4,col5 = st.columns(5)
  with col1:
    st.text(movie_name[0])
    st.image(movie_poster[0])
  with col2:
    st.text(movie_name[1])
    st.image(movie_poster[1])
  with col3:
    st.text(movie_name[2])
    st.image(movie_poster[2])
  with col4:
    st.text(movie_name[3])
    st.image(movie_poster[3])
  with col5:
    st.text(movie_name[4])
    st.image(movie_poster[4])
  
  col6, col7, col8, col9, col10 = st.columns(5)
  with col6:
    st.text(movie_name[5])
    st.image(movie_poster[5])
  with col7:
    st.text(movie_name[6])
    st.image(movie_poster[6])
  with col8:
    st.text(movie_name[7])
    st.image(movie_poster[7])
  with col9:
    st.text(movie_name[8])
    st.image(movie_poster[8])
  with col10:
    st.text(movie_name[9])
    st.image(movie_poster[9])