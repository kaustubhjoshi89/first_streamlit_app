import streamlit
streamlit.title('this is a sample app')
streamlit.header('this is a header')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')

import pandas

t1=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
t1=t1.set_index('Fruit')
streamlit.multiselect("filter",list(t1.index))
streamlit.dataframe(t1)
