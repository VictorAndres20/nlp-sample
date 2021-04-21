from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
# Derivacion regresiva con algoritmo de Porter


spanish_stemmer = SnowballStemmer('spanish')


# Porter only workds with englis words
def stem_proter(word):
    stemmer = PorterStemmer()
    return stemmer.stem(word)


def steam_spanish(word):
    return spanish_stemmer.stem(word)


def stem_tokens_cleaned_syn(tokens_cleaned_syn):
    return [steam_spanish(token) for token in tokens_cleaned_syn]
