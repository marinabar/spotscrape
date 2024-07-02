import unicodedata
import re

def remover(text):
    cleaned_text = []
    for char in text:
        if unicodedata.category(char).startswith('L') or char.isnumeric() or char.isspace():
            cleaned_text.append(char)
    return ''.join(cleaned_text)

def nostuff(text):

    search_keyword = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", text).replace("(", "").replace(")", "").replace("!", "")
    fin = search_keyword.replace("&", " ").replace("   ", " ").replace(',', "")
    return fin
