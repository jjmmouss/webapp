import streamlit as st

if st.session_state["authentication_status"]:
    st.write("Bienvenue dans la deuxième enigme")
else:
    st.switch_page("app.py")