import streamlit as sp



sp.set_page_config(
    layout="wide",
    page_title="MovieLens Data Analysis",
    page_icon="🎞️" # emoji Unicode directement
)
# Navigation

page_0 = sp.Page("page0.py",title="Home",icon="🏠") # film clapperboard
page_1 = sp.Page("page1.py",title="OverView",icon="🎞️") # film clapperboard
page_2 = sp.Page("page2.py",title="Tags Insights",icon="📊") #  Bar chart
# page_3 = sp.Page("page3.py",title="Movie Explorer",icon="🔎") # Magnifying glasss

# pg = sp.navigation([page_1,page_2,page_3])
pg = sp.navigation([page_0,page_1,page_2])
pg.run()