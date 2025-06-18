import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from streamlit import divider

st.header("st.write", divider='blue')

st.write("Hello :sunglasses:")
st.write(1234)
st.divider()

df = pd.DataFrame({
    'col1': [1, 2, 3, 4],
    'col2': [10, 20, 30, 40],
})
st.write(df)
st.divider()

st.write("Below is a DataFrame", df, "Above is a DataFrame")
st.divider()

df2 = pd.DataFrame(
    np.random.random((200, 3)),
    columns=['a', 'b', 'c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', color='c', size='c'
)
st.write(c)
