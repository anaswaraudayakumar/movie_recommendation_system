import streamlit as st
import pandas as pd 
import pickle
import numpy as np
import requests

movie_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movie_dict)
st.title ( 'Movie Recommendation System')


#poster 
def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=5f40eee700b2053631b0ce5cdfd578ea'.format(movie_id))
    data=response.json()
    
    return "https://image.tmdb.org/t/p/w500"+ data['poster_path']



#recommend from jupyter
def recommend(movie):
    movie_index=movies[movies['title'] == movie].index[0]
    distance=similarity[movie_index]
    movie_list=sorted(list(enumerate(distance)),reverse =True,key= lambda x :x[1])[1:6]
    
    recommended_movies=[]
    recommended_movies_poster =[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

similarity=pickle.load(open('similarity.pkl','rb'))

selected_movieName= st.selectbox( "Movies",movies['title'].values)

if st.button("Recommend",type="primary"):
    names,posters = recommend(selected_movieName)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
         st.text(names[1])
         st.image(posters[1])


    with col3:
         st.text(names[2])
         st.image(posters[2])

    with col4:
         st.text(names[3])
         st.image(posters[3])


    with col5:
         st.text(names[4])
         st.image(posters[4])





