from enigme_page_generation import generate_page
ENIGME_ID = 1
Instruction= """
### Consigne

Les lettres des cases bleues forment un anagrame, qui suis-je? (sans accent)
"""
generate_page(enigme_id=ENIGME_ID,enigme_instruction=Instruction)
