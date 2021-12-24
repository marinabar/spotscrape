import unicodedata
import re

def remover(text):
        text = unicodedata.normalize('NFD', text)\
            .encode('ascii', 'ignore')\
            .decode("utf-8")

        return str(text)

def nostuff(text):

    search_keyword = re.sub("([\(\[]).*?([\)\]])", "\g<1>\g<2>", text).replace("(", "").replace(")", "").replace("!", "")
    fin = search_keyword.replace("&", " ").replace("   ", " ").replace(',', "")
    return fin
