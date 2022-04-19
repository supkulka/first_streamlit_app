import streamlit
import requests

streamlit.title('My Mom\'s new healthy dinner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

fruits_selected=streamlit.multiselect("pick some fruits:",list(my_fruit_list.index),['Banana','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display table on page 
streamlit.dataframe(fruits_to_show)
streamlit.header('🍌🥭 Fruityvice Fruit Advice! 🥝🍇')
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice =streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The User entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
