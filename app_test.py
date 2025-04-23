import streamlit as st
import pandas as pd

st.title('Тест простого веб-приложения на базе Streamlit')

name = st.text_input('Введите имя', '')

st.write(f'Hello {name}!')

x = st.slider('Выбери дату', '2025-04-01', 23, '2025-04-23')

# df = pd.DataFrame({'x': [x], 'y': [y] , 'x + y': [x + y]}, index = ['addition row'])
st.write(x)
