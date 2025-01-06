import streamlit as st

st.header("Static File")

"""
As you learned in Streamlit fundamentals, Streamlit runs a server that clients connect to. That means viewers of your app don't have direct access to the files which are local to your app. 

Most of the time, this doesn't matter because Streamlt commands handle that for you. When you use `st.image(<path-to-image>)` your Streamlit server will access the file and handle the necessary hosting so your app viewers can see it. 

However, if you want a direct URL to an image or file you'll need to host it. This requires setting the correct configuration and placing your hosted files in a directory named static.
"""

st.code("""
        your-project/
        ├── static/
        │   └── my_hosted-image.png
        └── streamlit_app.py
        """, language="text")


"""
To learn more, read our guide on Static file serving. 
"""

st.link_button("Static File Configuration",
               "https://docs.streamlit.io/develop/concepts/configuration/serving-static-files")
