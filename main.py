from bs4 import BeautifulSoup
from markdown import markdown
import unicodedata as ud
import nltk

nltk.download('punkt')


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


markdown_file = 'data/work_v2.md'
rus_dict_file = 'data/dictionaries/rus.txt'

translating_strings = []
with open(markdown_file, 'r') as out:
    html = markdown(out.read())
    text = ''.join(BeautifulSoup(html, features="html.parser").findAll(text=True))
    for line in text.split('\n'):
        tokens = nltk.sent_tokenize(line)
        if len(tokens) > 0:
            for token in tokens:
                if not only_roman_chars(token):
                    translating_string = token.strip()
                    if translating_string not in translating_strings:
                        translating_strings.append(translating_string)


with open(rus_dict_file, "w") as output:
    for row in translating_strings:
        output.write(str(row) + '\n')

