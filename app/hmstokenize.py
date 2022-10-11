
import spacy
import textacy

nlp = spacy.load("en_core_web_lg")

def extract_tokens_from_text(menu_item, menu_description):
    combined_text = menu_item + " " + menu_description
#     print(menu_item)
#     print(menu_description)
#     print(combined_text)
    doc = nlp(combined_text.lower())

    tokens = textacy.extract.words(doc, 
            filter_stops = True,           # default True, no stopwords
            filter_punct = True,           # default True, no punctuation
            filter_nums = True,            # default False, no numbers
            include_pos = ['PROPN', 'NOUN', 'ADJ'], # default None = include all
            exclude_pos = None,            # default None = exclude none
            min_freq = 1)                  # minimum frequency of words
    words = list(textacy.extract.terms_to_strings(tokens, by="lemma"))
    return words
