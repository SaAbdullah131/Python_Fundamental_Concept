# streamlit first app.
import streamlit as st;
import pandas as pd;
import numpy as np;
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

# Display mathematical expression formatted as LaTex
# st.letex(r'''
#     a+ar+a r^2 + a r^3 + \ cdots + a r^{n-1} = 
#     \sum_{k=0}^{n-1} ar^k =
#     a\ letf(\frac{1-r^{n}}{1-1}\ right)
# '''
# )

st.write("Line Chart Streamlit using numpy and pandas library")
chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c']
)
st.line_chart(chart_data);

# code section streamlit
st.write("Writing code ....")
code ='''def hello():
     print("Hello, Streamlit !!!") 
#this is python code
'''
st.code(code,language='python')