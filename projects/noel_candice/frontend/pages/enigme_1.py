import streamlit as st

# TODO: Add return button to main_page
# TODO: Add saving credentials when solved
# TODO: Add gift when solved
if st.session_state["authentication_status"]:
    st.write("Bienvenue dans la première enigme")
else:
    st.switch_page("app.py")