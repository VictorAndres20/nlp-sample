from nltk.corpus import stopwords


def clean_tokens(tokens):
    tokens_cleaned = tokens[:]
    for token in tokens:
        if token in stopwords.words('spanish'):
            tokens_cleaned.remove(token)
    return tokens_cleaned
