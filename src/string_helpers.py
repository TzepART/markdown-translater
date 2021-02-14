import unicodedata as ud
from bs4 import BeautifulSoup
from markdown import markdown


def get_sorted_dictionaries_by_lists(keys_list, values_list) -> dict:
    sorted_dictionary = {}

    dictionary = dict(zip(keys_list, values_list))
    for k in sorted(dictionary, key=len, reverse=True):
        sorted_dictionary[k] = dictionary[k]

    return sorted_dictionary


def get_text_from_markdown(init_text):
    html = markdown(init_text)
    return ''.join(BeautifulSoup(html, features="html.parser").findAll(text=True))


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