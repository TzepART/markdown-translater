import unicodedata as ud
from bs4 import BeautifulSoup
from markdown import markdown
import nltk

nltk.download('punkt')


def get_sorted_dictionaries_by_lists(keys_list, values_list) -> dict:
    sorted_dictionary = {}

    dictionary = dict(zip(keys_list, values_list))
    for k in sorted(dictionary, key=len, reverse=True):
        sorted_dictionary[k] = dictionary[k]

    return sorted_dictionary


def get_text_from_markdown(init_text):
    html = markdown(init_text)
    return ''.join(BeautifulSoup(html, features="html.parser").findAll(text=True))


def add_language_items_to_list(language_items, str_line):
    tokens = nltk.sent_tokenize(str_line)
    if len(tokens) > 0:
        for token in tokens:
            if not only_roman_chars(token):
                language_item = token.strip()
                if language_item not in language_items:
                    language_items.append(language_item)


def is_latin(uchr):
    latin_letters = {}
    try:
        return latin_letters[uchr]
    except KeyError:
        return latin_letters.setdefault(uchr, 'LATIN' in ud.name(uchr))


def only_roman_chars(unistr):
    return all(is_latin(uchr)
               for uchr in unistr
               if uchr.isalpha())