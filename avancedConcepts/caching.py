import numpy as np
import pandas as pd
import streamlit as st

st.title('Avanced Concepts')

"""
Now that you know how a Streamlit app runs and handles data, let's talk about being efficient. Caching allows you to save the output of a function so you can skip over it on rerun. Session State lets you save information for each user that is preserved between reruns. This not only allows you to avoid unecessary recalculation, but also allows you to create dynamic pages and handle progressive processes.
"""

st.subheader('Caching')

"""
Caching allows your app to stay performant even when loading data from the web, manipulating large datasets, or performing expensive computations.

The basic idea behind caching is to store the results of expensive function calls and return the cached result when the same inputs occur again. This avoids repeated execution of a function with the same input values.

To cache a function in Streamlit, you need to apply a caching decorator to it. You have two choices:

* `st.cache_data` is the recommended way to cache computations that return data. Use `st.cache_data` when you use a function that returns a serializable data object  . It creates a new copy of the data at each function call, making it safe against mutations and race conditions. The behavior of `st.cache_data` is what you want in most cases – so if you're unsure, start with `st.cache_data` and see if it works!

* `st.cache_resource` is the recommended way to cache global resources like ML models or database connections. Use `st.cache_resource` when your function returns unserializable objects that you don’t want to load multiple times. It returns the cached object itself, which is shared across all reruns and sessions without copying or duplication. If you mutate an object that is cached using `st.cache_resource`, that mutation will exist across all reruns and sessions.
"""


@st.cache_data
def long_running_function(param1, param2):
    pass


"""
In the above example, `long_running_function` is decorated with `@st.cache_data`. As a result, Streamlit notes the following:

The name of the function ("`long_running_function`").
The value of the inputs (param1, param2).
The code within the function.

Before running the code within `long_running_function`, Streamlit checks its cache for a previously saved result. If it finds a cached result for the given function and input values, it will return that cached result and not rerun function's code. Otherwise, Streamlit executes the function, saves the result in its cache, and proceeds with the script run. During development, the cache updates automatically as the function code changes, ensuring that the latest changes are reflected in the cache.
"""

st.image("../img/caching-high-level-diagram.png")
