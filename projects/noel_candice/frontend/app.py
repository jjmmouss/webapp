import streamlit as st
from streamlit_authenticator import Authenticate
import yaml
from yaml.loader import SafeLoader
from background import set_bg_hack
from cadenas_utils import CADENAS_NAMES




with open("projects/noel_candice/frontend/crendentials.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

set_bg_hack("projects/noel_candice/frontend/images/background_noel_blanc.jpg")
st.write("Pour un Joyeux Noel")
try:
    authenticator.login()
except Exception as e:
    st.error(e)


if st.session_state["authentication_status"]:
    authenticator.logout(location="sidebar")
    for cadenas_name in CADENAS_NAMES:
        st.session_state[cadenas_name] = config["credentials"]["usernames"][st.session_state["username"]][cadenas_name]    
    
    if st.button(label="Prete pour l'aventure ?",key="start"):
        st.switch_page("pages/main_page.py")

elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')

# # Create a simple web app with Streamlit
# st.title("Name Input App")

# # Text input for user's name
# name = st.text_input("Enter your name:")

# # Button to submit
# if st.button("Submit"):
#     if name:
#         st.write(f"Hello, {name}!")
#     else:
#         st.write("Please enter your name.")
