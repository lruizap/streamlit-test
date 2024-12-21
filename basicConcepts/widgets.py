import numpy as np
import pandas as pd
import streamlit as st

st.title('Widgets')

"""
When you've got the data or model into the state that you want to explore, you can add in widgets like `st.slider()`, `st.button()` or `st.selectbox()`
"""

num = st.slider('Number')  # 👈 this is a widget
st.write(num, 'squared is', num * num)

"""
---
"""

"""
Widgets can also be accessed by key, if you choose to specify a string to use as the unique key for the widget
"""

st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

"""
Every widget with a key is automatically added to Session State.
"""

"""
---
"""

st.subheader('Use checkboxes to show/hide data')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

if st.checkbox('Show dataframe'):
    st.table(chart_data)

"""
---
"""

st.subheader('Use a selectbox for options')

"""
Use `st.selectbox` to choose from a series. You can write in the options you want, or pass through an array or data frame column.
"""

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column'])

# ? No es necesario poner `st.write`

st.write('You selected: ', option)
