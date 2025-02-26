import streamlit as st
import pandas as pd
import random

df = pd.read_csv('movies_Maria.csv')

st.logo('./images/film.jpg', icon_image='./images/roll.png', size='large')

st.title('Сервис для случайной генерации фильмов 🎥')

st.write('### Нажмите кнопку, если хотите испытать судьбу!')

if 'num_list' not in st.session_state:
    st.session_state.num_list = None

if st.button('### 🍀 Попытать удачу 🍀'):
    st.session_state.num_list = [random.randint(0, 666) for _ in range(10)]
    
if st.session_state.num_list is not None: 
    st.write('#### Вы сами на это напросились!')
    st.write('Для отображения описания нужно кликнуть на кнопку с названием')
    for num in st.session_state.num_list:
        if st.button(f'{df.loc[num]['movie_title']}'):
            st.write(f'#### Описание: \n{df.loc[num]['description']}\n')
        
    
