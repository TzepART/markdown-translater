markdown_file = 'data/work_v2.md'
en_markdown_file = 'data/work_v2_en.md'
rus_dict_file = 'data/dictionaries/rus.txt'
en_dict_file = 'data/dictionaries/en.txt'


with open(rus_dict_file, 'r') as out:
    keys = map(lambda s: s.strip(), out.readlines())


with open(en_dict_file, 'r') as out:
    values = map(lambda s: s.strip(), out.readlines())

dictionary = dict(zip(keys, values))


sorted_dictionary = {}
for k in sorted(dictionary, key=len, reverse=True):
    sorted_dictionary[k] = dictionary[k]

with open(markdown_file, 'r') as out:
    new_text = out.read()
    for word, initial in sorted_dictionary.items():
        new_text = new_text.replace(word, initial)

with open(en_markdown_file, "w") as output:
    output.write(new_text)

