import streamlit as st

#Take a user Input\
name= st.text_input("Enter your name")

st.title("Take the input")

if st.button("submit"):
  st.write(f"print the name:(name)")
