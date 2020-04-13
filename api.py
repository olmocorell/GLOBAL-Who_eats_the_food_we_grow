import src.cleandata as clean
import streamlit as st
from PIL import Image

st.markdown("<h1 style='text-align: center; color: black;'>Who eats the food we grow?</h1>", unsafe_allow_html=True)

image = Image.open('input/portadapi.jpg')
st.image (image,use_column_width=True)
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
param_area = "Area"
area = st.selectbox(
    'Choose an area to visualize data',
     clean.choice(param_area))
'You selected: ', area

#select box for choose item
param_item = "Item"
item = st.selectbox(
    'Select the product to see the production evolution',
    clean.choice(param_item)
)
'You selected: ', item


datagraf = clean.grafico(area,item)
"""
In the first graph, you can see the evolution of product production in the country you have selected.
"""
st.line_chart(datagraf)
"""
In the second graph, you can see the exact amount in k tons of that product (feed and food).
You can pass the mouse over it and see the value.
If you are really interested in this data, you can interact with the graph to see it bigger or smaller or even download it.
"""
st.bar_chart(datagraf)

