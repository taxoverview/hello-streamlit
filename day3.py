import streamlit as st

st.header("Button")

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Bye")
