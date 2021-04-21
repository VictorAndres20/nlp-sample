from src.steps.first_text_clasification.tokenizer import tokenize
from src.steps.first_text_clasification.stop_words import clean_tokens
from src.steps.first_text_clasification.synonyms_antonyms import build_synonyms_manual, replace_syn
from src.steps.first_text_clasification.word_stemming import stem_tokens_cleaned_syn


# MAIN
def main():
    print(f'Hi')
    tokens = tokenize()
    tokens_cleaned = clean_tokens(tokens)
    tokens_cleaned_syn = replace_syn("libertad", build_synonyms_manual(), tokens_cleaned)
    tokens_cleaned_syn_stem = stem_tokens_cleaned_syn(tokens_cleaned_syn)
    print(tokens_cleaned_syn_stem)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
