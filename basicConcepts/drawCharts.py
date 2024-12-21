import numpy as np
import pandas as pd
import streamlit as st

st.title('Draw Charts and maps')

"""
Streamlit supports several popular data charting libraries like Matplotlib, Altair, deck.gl, and more. In this section, you'll add a bar chart, line chart, and a map to your app.
"""

st.subheader('Draw a line chart')

"""
You can easily add a line chart to your app with `st.line_chart()`. We'll generate a random sample using Numpy and then chart it.
"""

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"""
---
"""

st.subheader('Plot a map')

"""
With `st.map()` you can display data points on a map. Let's use Numpy to generate some sample data and plot it on a map of San Francisco.
"""

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)
