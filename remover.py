from unidecode import unidecode

def remover(text):

        #convert plain text to utf-8
        u = unidecode(text, "utf-8")
        #convert utf-8 to normal text
        return unidecode(u)