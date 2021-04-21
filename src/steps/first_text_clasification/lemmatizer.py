from nltk.stem import WordNetLemmatizer
import spacy

lemmatizer = WordNetLemmatizer()
nlp = spacy.blank("es")
# nlp = spacy.load('es_core_news_sm')


def lemmatize_english(word, pos='v'):
    # pos 'v' = verbs
    lemmatizer.lemmatize(word, pos=pos)


def lemmatize_spanish(tokens_cleaned_syn):
    tokens_cleaned_syn_lem = []
    separator = ' '
    for token in nlp(separator.join(tokens_cleaned_syn)):
        tokens_cleaned_syn_lem.append(token.lemma_)

    return tokens_cleaned_syn_lem
