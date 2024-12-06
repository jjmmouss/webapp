import streamlit as st
from app import authenticator,NB_CADENAS
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
    st.write(f'Welcome *{st.session_state["name"]}*')
    cols= st.columns([1]*NB_CADENAS)
    for cadenas_id,col in enumerate(cols):
        with col:
            if not st.session_state[f"cadenas_{cadenas_id}_unlock"]:
                if st.button(f"cadenas_{cadenas_id+1}"):
                    st.switch_page(f"pages/enigme_{cadenas_id+1}")
            else:
                st.write(f"Cadenas {cadenas_id+1} unlocked")
    if all([st.session_state[f"cadenas_{cadenas_id}_unlock"] for cadenas_id in range(NB_CADENAS)]):
        st.write("JOYEUX NOEL!!!!!!!")

else:
    st.switch_page("app.py")