import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

# Définition du dossier de sortie
OUTPUT_DIR=Path(__file__).resolve().parent.parent / "output"

st.title("📊Tags Insights")

#fonction pour charger les fichiers parquet
@st.cache_data
def loa_parquet_data(file_name):
    file_path=OUTPUT_DIR /file_name
    return pd.read_parquet(file_path)

# chargementdes données
tags_good_rating=loa_parquet_data("tags_good_rating.parquet")
tags_compare=loa_parquet_data("tags_compare.parquet")
tags_by_genre=loa_parquet_data("tags_by_genre.parquet")
user_tag=loa_parquet_data("user_tag_stats.parquet")

#graphique 1 : pourcentages des tags
fig_tag=px.pie(tags_good_rating, values ='count', names ='tag', title ='Pourcentages des films bien notés')
#st.plotly_chart(fig_tag,use_container_width=True)


# graphique 2: Comparaison des Tags : Films bien notés vs mal notés
fig3 = px.bar(
     tags_compare.melt(id_vars="tag", value_vars=["count_good", "count_bad"],
                         var_name="Type", value_name="count"),
    x="count",
    y="tag",
    color="Type",
    barmode="group",
    title="Comparaison des Tags : Films bien notés vs mal notés",
    labels={"count": "Nombre d’occurrences", "tag": "Tag"}
)
fig3.update_layout(yaxis={'categoryorder':'total ascending'}, height=600)

#graphique 3:top tag des films utilisés pa les utilisateurs

fig4 = px.bar(
    user_tag,
    x="tag",
    y="count",
    title="Top tags utilisés par les utilisateurs",
    labels={"count": "Nombre d’utilisations", "tag": "Tag"},
)

fig4.update_layout(yaxis={'categoryorder': 'total ascending'})

## affichage des résultats
col1, col2=st.columns([1,2])

with col1:
    st.plotly_chart(fig_tag,use_container_width=True)
    

with col2:
   st.plotly_chart(fig3,use_container_width=True)
    
st.plotly_chart(fig4,use_container_width=True)  

st.divider()
