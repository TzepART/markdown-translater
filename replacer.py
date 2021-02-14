from src.file_helpers import get_strip_lines_by_file
from src.string_helpers import get_sorted_dictionaries_by_lists


markdown_file = 'data/readme.md'
en_markdown_file = 'data/readme_en.md'
rus_dict_file = 'data/dictionaries/rus.txt'
en_dict_file = 'data/dictionaries/en.txt'


keys = get_strip_lines_by_file(rus_dict_file)
values = get_strip_lines_by_file(en_dict_file)

sorted_dictionary = get_sorted_dictionaries_by_lists(keys, values)

with open(markdown_file, 'r') as out:
    new_text = out.read()
    for word, initial in sorted_dictionary.items():
        new_text = new_text.replace(word, initial)

with open(en_markdown_file, "w") as output:
    output.write(new_text)

