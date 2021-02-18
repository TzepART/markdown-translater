from src.file_helpers import FilePathsData, get_strip_lines_by_file, get_text_by_file, write_text_to_file
from src.string_helpers import get_sorted_dictionaries_by_lists

keys = get_strip_lines_by_file(FilePathsData.rus_dict_file)
values = get_strip_lines_by_file(FilePathsData.en_dict_file)

sorted_dictionary = get_sorted_dictionaries_by_lists(keys, values)

new_text = get_text_by_file(FilePathsData.markdown_file)
for word, initial in sorted_dictionary.items():
    new_text = new_text.replace(word, initial)

write_text_to_file(new_text, FilePathsData.en_markdown_file)
