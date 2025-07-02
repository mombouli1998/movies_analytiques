import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

# Définition du dossier de sortie
OUTPUT_DIR=Path(__file__).resolve().parent.parent / "output"

st.title("🎞️ Analyse Générale des Films et Évaluations")

# fonction cache pour charger les fichiers parquet
@st.cache_data
def load_parquet_data(file_name):
    file_path= OUTPUT_DIR / file_name
    return pd.read_parquet(file_path)

# chargement des données
genre_df=load_parquet_data("genredf.parquet")
#st.write(genre_df)

# chargement des datasets
#genre_rating_stats=load_parquet_data("genre_rating_stats.parquet")

movies_by_year=load_parquet_data("movies_by_year.parquet")
#st.write(movies_by_year)

top_movies=load_parquet_data("top_movies_by_ratings.parquet")
#st.write(top_movies)
#ratings_df=load_parquet_data("ratings.parquet")

# Graphique 1 : TOP 10 genres par nombre de films
fig_genre=px.bar(
    genre_df,
    x="count",
    y="genre",
    title="TOP 10 genres par nombre de films",
    labels={"genre":"Genre","count":"Nombre de films"},
    color="count",
    color_continuous_scale="viridis",
    orientation='h'
)
fig_genre.update_layout(
    yaxis={'categoryorder':'total ascending'},
    height=350
)

#st.plotly_chart(fig_genre,use_container_width=True)

# graphique 4: Top 20 des films par nombre d'évaluations
fig_film = px.bar(
    top_movies.sort_values("rating_count", ascending=True),  # Pour affichage de bas en haut
    x="rating_count",
    y="title",
    color="avg_rating",
    orientation="h",
    title="Top 20 des films par nombre d'évaluations",
    labels={
        "title": "Titre du film",
        "rating_count": "Nombre d'évaluations",
        "avg_rating": "Note moyenne"
    },
    color_continuous_scale="viridis"
)

fig_film.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=700
)

#st.plotly_chart(fig_film,use_container_width=True)

#graphique 5: Nombre de film par année
fig_film_year = px.bar(
    movies_by_year,
    x="year",
    y="movie_count",
    title="Nombre total de films par année (basé sur le titre)",
    labels={"year": "Année", "movie_count": "Nombre de films"},
)

fig_film_year.update_layout(
    xaxis_title="Année",
    yaxis_title="Nombre de films",
    height=500
)

#st.plotly_chart(fig_film_year,use_container_width=True)

# mise en page Streamlit
col1, col2=st.columns([1,2])

with col1:
    st.plotly_chart(fig_genre,use_container_width=True)
    

with col2:
   st.plotly_chart(fig_film,use_container_width=True)
    
st.plotly_chart(fig_film_year,use_container_width=True)  

st.divider()
##