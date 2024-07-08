import streamlit as st
from langchain_project import name_and_items

st.title('restaurant name Generator')
country = st.sidebar.selectbox('pick a country',
                               ('Bangladesh', 'India', 'Pakistan', 'Itali', 'America'))

response = name_and_items(country)
restaurent_name = response['restaurent_name']


st.header(f'****---{restaurent_name}---****')
st.write('---The food menu items---')
food_items = response['food_items'].strip().split('\n')

for menu in food_items:
    if menu != " " or menu != restaurent_name:
        st.write(menu)
