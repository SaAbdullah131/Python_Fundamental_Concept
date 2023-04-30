# streamlit first app.
import streamlit as st;
import pandas as pd;
#Title
st.title('My First Streamlit app');

# Header
st.header('Second Line');

#Markdown
st.markdown('Hi ! There');

# success text --green
st.success("YaY ! This wan Success !!!")

# erro text -- red
st.error('OOPs!! That Wat an Error');

# write in streamlit
st.write('Hello, *SA Abdullah* :happy')

# st.write() also accepts other data formats
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))