import unicodedata

def remover(text):
        text = unicodedata.normalize('NFD', text)\
            .encode('ascii', 'ignore')\
            .decode("utf-8")

        return str(text)
