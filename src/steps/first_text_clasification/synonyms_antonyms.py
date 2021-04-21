from nltk.corpus import wordnet
from src.utils.frequency import build_freq, print_freq


def build_synonyms_wordnet(word):
    # By now, 2021, wordnet only works with english words
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())

    return synonyms


def build_synonyms_manual():
    return ['libertad', 'independencia']


def replace_syn(word, synonyms, tokens_cleaned):
    tokens_cleaned_syn = []
    for i, syn in enumerate(synonyms):
        tokens_cleaned_syn = [token.replace(synonyms[i], word) for token in tokens_cleaned]

    # freq = build_freq(tokens_cleaned_syn)
    # print_freq(freq)
    return tokens_cleaned_syn
