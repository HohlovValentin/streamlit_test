import streamlit as st
import pandas as pd
import datetime as dt
from dateutil.relativedelta import relativedelta # to add days or years

st.title('Тест простого веб-приложения на базе Streamlit')

name = st.text_input('Введите имя', '')

st.write(f'Hello {name}!')

## Range selector
cols1,_ = st.beta_columns((1,2)) # To make it narrower
format = 'MMM DD, YYYY'  # format output
start_date = dt.date(year=2021,month=1,day=1)-relativedelta(years=2)  #  I need some range in the past
end_date = dt.datetime.now().date()-relativedelta(years=2)
max_days = end_date-start_date

slider = cols1.slider('Select date', min_value=start_date, value=end_date ,max_value=end_date, format=format)
## Sanity check
st.table(pd.DataFrame([[start_date, slider, end_date]],
              columns=['start',
                       'selected',
                       'end'],
              index=['date']))
