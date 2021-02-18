from src.string_helpers import get_text_from_markdown, add_language_items_to_list
from src.file_helpers import FilePathsData, write_list_to_file, get_text_by_file

translating_strings = []

text = get_text_from_markdown(get_text_by_file(FilePathsData.markdown_file))

for line in text.split('\n'):
    add_language_items_to_list(translating_strings, line)

write_list_to_file(translating_strings, FilePathsData.rus_dict_file)
