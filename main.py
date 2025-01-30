import streamlit as st
import pickle
import pandas as pd
import requests

#this function help to fetch the poster from dataset
def fetch_post(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500'+data['poster_path']


def recommand(movie):
  index = movie_dict[movie_dict['title'] == movie ].index[0]
  distance = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])[1:6]
  recom = []
  movie_poster = []
  for i in distance:
      movie_id = movie_dict.iloc[i[0]].movie_id
      #fetching movie post
      movie_poster.append(fetch_post(movie_id))
      recom.append(movie_dict.iloc[i[0]]['title'])
  return recom, movie_poster

similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = pickle.load(open('movie_dict.pkl','rb'))
movie_dict = pd.DataFrame(movie_list)

st.title("Movie Recommanded System Content Base")
option = st.selectbox(
    'how would you like to select?',
    movie_dict['title']
)
if st.button("Recommand"):
     name, poster = recommand(option)
     col1, col2, col3, col4, col5 = st.columns(5)
     with col1:
         st.write(name[0])
         st.image(poster[0])
     with col2:
         st.write(name[1])
         st.image(poster[1])
     with col3:
         st.write(name[2])
         st.image(poster[2])
     with col4:
         st.write(name[3])
         st.image(poster[3])
     with col5:
         st.write(name[4])
         st.image(poster[4])