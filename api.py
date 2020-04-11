import src.cleandata as clean
import streamlit as st
import pandas as pd

st.title("Who eats the food we grow?")
st.write(
"""
In this visualization project, I have created an API that allows us to see the data of the production of different foods in the countries and if they are used for food or feed. I have extracted the data from [this Kaggle dataset.](https://www.kaggle.com/dorbicycle/world-foodfeed-production)
"""
)

@st.cache(persist=True)
def load_data():
    data = clean.loadCleanData()
    return data
#load all data
data = load_data()

#select box for choose country
area = "Area"
option = st.selectbox(
    'Choose an area to visualize data',
     clean.choice(area))
'You selected: ', option

#select box for choose item
item = "Item"
option2 = st.selectbox(
    'Select the product to see the production evolution',
    clean.choice(item)
)
'You selected: ', option2

