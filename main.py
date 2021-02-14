from src.string_helpers import only_roman_chars, get_text_from_markdown
import nltk

nltk.download('punkt')

markdown_file = 'data/readme.md'
rus_dict_file = 'data/dictionaries/rus.txt'

translating_strings = []

with open(markdown_file, 'r') as out:
    text = get_text_from_markdown(out.read())
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
