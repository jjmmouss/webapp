# import streamlit as st
# from cadenas_utils import CADENAS_NAMES,validate_answer, get_cadenas_name_for_enigme,get_answer_for_enigme
# # TODO: Add return button to main_page
# # TODO: Add saving credentials when solved
# # TODO: Add gift when solved
# ENIGME_ID=0
# CADENAS_NAME = get_cadenas_name_for_enigme(enigme_id=ENIGME_ID)
# ANSWER = get_answer_for_enigme(enigme_id=ENIGME_ID)
# if st.session_state["authentication_status"]:
#     st.write("Bienvenue dans la première enigme")
    
#     answer = st.text_input("Ta réponse")
#     if st.button("submit"):
#         if answer==ANSWER:
#             st.session_state[CADENAS_NAME]=True
#             #Save credential
#     if st.session_state[CADENAS_NAME]:
#         st.write("BRAVO!")
#         if st.button("Return to main page"):
#             st.switch_page("pages/main_page.py")
# else:
#     st.switch_page("app.py")
from enigme_page_generation import generate_page
ENIGME_ID = 0

instruction = """
### Consigne

**Un voisin est une case adjacente, les diagonales ne comptent pas.**

Trouve les nombres en te basant sur leur description :

1. **Je n'ai que 3 voisins qui sont les suivants : 1, 1, et 7.**  
2. **Je suis au centre de mon carré et mes voisins sont : 2, 6, 7, 9.**  
3. **Je suis à l'intersection de la 2ᵉ colonne et de la 9ᵉ ligne**  
   *(la case en haut à gauche correspond à la 1ʳᵉ ligne, 1ʳᵉ colonne).*  
4. **Je suis le plus petit des quatre nombres des coins du carré central.**
"""
generate_page(enigme_id=ENIGME_ID,enigme_instruction=instruction)

