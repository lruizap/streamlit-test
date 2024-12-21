import numpy as np
import pandas as pd
import streamlit as st

st.title('Layouts')

"""
Streamlit makes it easy to organize your widgets in a left panel sidebar with `st.sidebar()`. Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app while still having access to UI controls.
"""

st.sidebar.title('Widgets')

st.sidebar.write('---')
st.sidebar.subheader('`st.sidebar.selectbox()`')

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

st.sidebar.write('---')
st.sidebar.subheader('`st.sidebar.slider()`')

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

"""
---
"""

"""
Beyond the sidebar, Streamlit offers several other ways to control the layout of your app. st.columns lets you place widgets side-by-side, and st.expander lets you conserve space by hiding away large content.
"""

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

"""
> `st.echo()` and `st.spinner()` are not currently supported inside the sidebar or layout options. Rest assured, though, we're currently working on adding support for those too!
"""
