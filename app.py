import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=b2d31fbf794994375b05c3e3849f3875&language=en-US".format(movie_id)
    headers = {"User-Agent": "Mozilla/5.0"}  # ✅ Avoid getting blocked by TMDB
    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()
        if 'poster_path' in data and data['poster_path'] is not None:
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"





def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:9]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # FIXED: use movie_id from DataFrame
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies_dict= pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)

similarity= pickle.load(open('similarity.pkl', 'rb'))

st.title("Movie Recommends")

selected_movie_name= st.selectbox(
    'which movie do you want to watch',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])

    cols = st.columns(4)
    for i in range(4, 8):
        with cols[i - 4]:
            st.text(names[i])
            st.image(posters[i])

