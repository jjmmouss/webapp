import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate
from background import set_bg_hack

with open("crendentials.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
)

set_bg_hack("background/noel_blanc.jpg")
st.write("Pour un Joyeux Noel")
try:
    authenticator.login()
except Exception as e:
    st.error(e)


if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
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
