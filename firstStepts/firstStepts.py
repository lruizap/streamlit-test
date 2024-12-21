import numpy as np
import pandas as pd
import streamlit as st

from fetchData import loadData


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/''streamlit-demo-data/uber-raw-data-sep14.csv.gz')

st.title('Uber pickups in NYC')

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load 10,000 rows of data into the dataframe.
data = loadData(nrows=10000, column=DATE_COLUMN, data=DATA_URL)

# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data')
st.write(data)

