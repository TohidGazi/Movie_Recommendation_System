import base64
import pickle
import pandas as pd
import streamlit as st
import requests




def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'img.png'
sidebar_bg(side_bg)


st.sidebar.success("")



movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}'
                            '?api_key=bcca35fe996b8b4a073dae639617d566&language=en-US'.format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/original" + data['poster_path']






def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommended_movie, recommended_movie_posters



selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)


if st.button('Recommend'):
    recommended_movie, recommended_movie_posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(recommended_movie[0])
        st.image(recommended_movie_posters [0])
    with col2:
        st.header(recommended_movie[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.header(recommended_movie[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.header(recommended_movie[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.header(recommended_movie[4])
        st.image(recommended_movie_posters[4])








