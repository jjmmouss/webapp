import streamlit as st
from cadenas_utils import get_cadenas_name_for_enigme,get_answer_for_enigme,save_lock_status
# TODO: Add return button to main_page
# TODO: Add saving credentials when solved
# TODO: Add gift when solved

def generate_page(enigme_id:int):
    cadenas_name = get_cadenas_name_for_enigme(enigme_id=enigme_id)
    correct_answer = get_answer_for_enigme(enigme_id=enigme_id)
    if st.session_state["authentication_status"]:
        st.write(f"Bienvenue dans l'enigme numéro {enigme_id+1}")
        
        user_answer = st.text_input("Ta réponse")
        if st.button("submit"):
            if user_answer==correct_answer:
                st.session_state[cadenas_name]=True
                save_lock_status()
            else:
                st.error("Mauvaise réponse! Essaye encore ;)")
        if st.session_state[cadenas_name]:
            st.write("BRAVO!")
            if st.button("Return to main page"):
                st.switch_page("pages/main_page.py")
    else:
        st.switch_page("app.py")