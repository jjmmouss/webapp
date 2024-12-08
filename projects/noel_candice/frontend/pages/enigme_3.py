from enigme_page_generation import generate_page
ENIGME_ID = 2
Instruction= """
### Consigne

seul le prénom compte (sans accent)
"""
generate_page(enigme_id=ENIGME_ID,enigme_instruction=Instruction)
