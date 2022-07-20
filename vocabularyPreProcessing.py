#funcao para formatar os termos de um vocabulario:

import unidecode
import string 

def termFormater(term):
    term = term.lower()
    term = unidecode.unidecode(term)
    term = term.translate(str.maketrans('', '', string.punctuation))
    return term