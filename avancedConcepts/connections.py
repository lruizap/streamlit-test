import numpy as np
import pandas as pd
import streamlit as st

st.title('Connections')

"""
As hinted above, you can use `@st.cache_resource` to cache connections. This is the most general solution which allows you to use almost any connection from any Python library. However, Streamlit also offers a convenient way to handle some of the most popular connections, like SQL! `st.connection` takes care of the caching for you so you can enjoy fewer lines of code. Getting data from your database can be as easy as:
"""


# Mostrar el código sin ejecutarlo
st.code("""
  conn = st.connection("my_database")
  df = conn.query("select * from my_table")
  st.dataframe(df)
""", language="python")


"""
Of course, you may be wondering where your username and password go. Streamlit has a convenient mechanism for Secrets management. For now, let's just see how `st.connection` works very nicely with secrets. In your local project directory, you can save a `.streamlit/secrets.toml` file. You save your secrets in the `toml` file and `st.connection` just uses them! For example, if you have an app file streamlit_app.py your project directory may look like this:
"""

st.code("""
your-LOCAL-repository/
├── .streamlit/
│   └── secrets.toml # Make sure to gitignore this!
└── streamlit_app.py
""", language="plaintext")

"""
For the above SQL example, your `secrets.toml` file might look like the following:
"""

st.code("""
    [connections.my_database]
        type="sql"
        dialect="mysql"
        username="xxx"
        password="xxx"
        host="example.com" # IP or URL
        port=3306 # Port number
        database="mydb" # Database name
""", language='toml')


"""
Since you don't want to commit your `secrets.toml` file to your repository, you'll need to learn how your host handles secrets when you're ready to publish your app. 

Each host platform may have a different way for you to pass your secrets. 

If you use Streamlit Community Cloud for example, each deployed app has a settings menu where you can load your secrets. 

After you've written an app and are ready to deploy, you can read all about how to Deploy your app on Community Cloud.
"""
