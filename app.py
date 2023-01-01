import pickle
import streamlit as st
import requests

def get_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=495a9aa8bc967b61113522e39d77b1c6&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def get_info(movie_id):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=495a9aa8bc967b61113522e39d77b1c6&language=en-US"
    data=requests.get(url)
    data=data.json()
    ov=data["overview"]
    return ov

def get_vid(movie_id):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key=495a9aa8bc967b61113522e39d77b1c6&language=en-US"
    data= requests.get(url)
    data= data.json()
    try:
        vid_url="https://www.youtube.com/watch?v="+data["results"][0]["key"]
    except Exception:
        vid_url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    return vid_url


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    over=[]
    urls=[]
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].id
        recommended_movie_posters.append(get_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        over.append(get_info(movie_id))
        urls.append(get_vid(movie_id))


    return recommended_movie_names,recommended_movie_posters,over,urls


st.header('Movie Recommender')
movies = pickle.load(open('data.pkl','rb'))
similarity = pickle.load(open('sim.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,movie_overview,trailer_url = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.write(f"[Trailer]({trailer_url[0]})")
        st.markdown(movie_overview[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.write(f"[Trailer]({trailer_url[1]})")
        st.markdown(movie_overview[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.write(f"[Trailer]({trailer_url[2]})")
        st.markdown(movie_overview[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.write(f"[Trailer]({trailer_url[3]})")
        st.markdown(movie_overview[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.write(f"[Trailer]({trailer_url[4]})")
        st.markdown(movie_overview[4])
