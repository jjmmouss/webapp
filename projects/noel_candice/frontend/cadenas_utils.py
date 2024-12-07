import streamlit as st
import yaml
from yaml.loader import SafeLoader

NB_CADENAS = 3
CADENAS_NAMES = [f"cadenas_{cadenas_nb}_unlock" for cadenas_nb in range(NB_CADENAS)]
ANSWERS = ["1234","plop","coucou"]



def get_cadenas_name_for_enigme(enigme_id:int)->str:
    return CADENAS_NAMES[enigme_id]
def get_answer_for_enigme(enigme_id:int)->str:
    return ANSWERS[enigme_id]
def validate_answer(enigme_id:int):
    pass
def reset_locks():
    for cadenas_name in CADENAS_NAMES:
        st.session_state[cadenas_name] = False
    save_lock_status()
    
def save_lock_status():
    config_file_path = "projects/noel_candice/frontend/crendentials.yaml"
    with open(config_file_path) as file:
        config = yaml.load(file, Loader=SafeLoader)
    for cadenas_name in CADENAS_NAMES:
        config["credentials"]["usernames"][st.session_state["username"]][cadenas_name] = st.session_state[cadenas_name]
    
    with open(config_file_path, "w") as f:
        yaml.dump(config,f)