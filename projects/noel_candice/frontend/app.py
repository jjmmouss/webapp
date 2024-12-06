import streamlit as st

# Create a simple web app with Streamlit
st.title("Name Input App")

# Text input for user's name
name = st.text_input("Enter your name:")

# Button to submit
if st.button("Submit"):
    if name:
        st.write(f"Hello, {name}!")
    else:
        st.write("Please enter your name.")
