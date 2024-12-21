import pandas as pd
import streamlit as st

"""
Then save the script, and Streamlit will automatically rerun your app. Since this is the first time you’re running the script with '@st.cache_data', you won't see anything change. Let’s tweak your file a little bit more so that you can see the power of caching.
"""

@st.cache_data
def loadData(column, data, nrows):
    data = pd.read_csv(data, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    
    data.rename(lowercase, axis='columns', inplace=True)
    
    data[column] = pd.to_datetime(data[column])
    
    return data