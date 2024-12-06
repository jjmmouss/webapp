import streamlit as st

if st.session_state["authentication_status"]:
    st.write("Bienvenue dans la troisième enigme")
else:
    st.switch_page("app.py")