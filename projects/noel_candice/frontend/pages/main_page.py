import streamlit as st
from app import authenticator
from cadenas_utils import CADENAS_NAMES, NB_CADENAS, reset_locks
import numpy as np

st.markdown("""
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """, unsafe_allow_html=True)
if st.session_state["authentication_status"]:
    authenticator.logout(key="main_logout",location="sidebar")
    if st.sidebar.button("Reset Locks"):
        reset_locks()
    st.write(f'Welcome *{st.session_state["name"]}*')
    
    cadenas_state = [st.session_state[cadenas_name] for cadenas_name in CADENAS_NAMES]
    nb_unlocked_cadenas = np.sum(cadenas_state)


    st.image(f"projects/noel_candice/frontend/images/coffre_{NB_CADENAS-nb_unlocked_cadenas}_cadenas.png",caption=f"pirate chest with {NB_CADENAS-nb_unlocked_cadenas} locks")
    
    
    
    cols= st.columns([1]*len(CADENAS_NAMES))
    for cadenas_id,col in enumerate(cols):
        with col:
            if not st.session_state[f"cadenas_{cadenas_id}_unlock"]:
                if st.button(f"cadenas_{cadenas_id+1}"):
                    st.switch_page(f"pages/enigme_{cadenas_id+1}.py")
            else:
                st.write(f"Cadenas {cadenas_id+1} unlocked")
    if all(cadenas_state):
        st.write("JOYEUX NOEL!!!!!!!")

else:
    st.switch_page("app.py")