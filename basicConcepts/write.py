import numpy as np
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.title('My first app')

# Puedes usar estos comentarios -> """ Comentario """ Para escribir texto markdown en la app

st.subheader('My first DataFrame')

"""
Any time that Streamlit sees a variable or a literal value on its own line, it automatically writes that to your app using `st.write()`

Magic and `st.write()` inspect the type of data that you've passed in, and then decide how to best render it in the app. Sometimes you want to draw it another way. For example, instead of drawing a dataframe as an interactive table, you may want to draw it as a static table by using `st.table(df)`.
"""

st.write(df)

"""
There are other data specific functions like `st.dataframe()` and `st.table()` that you can also use for displaying data.
"""

st.table(df)

"""
This example uses Numpy to generate a random sample, but you can use Pandas DataFrames, Numpy arrays, or plain Python arrays.
"""

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

"""
Let's expand on the first example using the Pandas `Styler` object to highlight some elements in the interactive table.
"""

dfStyler = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dfStyler.style.highlight_max(axis=0))

"""
Streamlit also has a method for static table generation: st.table().
"""

st.table(dfStyler)
