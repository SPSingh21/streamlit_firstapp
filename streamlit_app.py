import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣🥑Omega 3 and Bueberry Oatmeals')
streamlit.text('🥗 Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard-Boiled free range eggs')
streamlit.text('🥑 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
