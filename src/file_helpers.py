from collections import Iterator
from dataclasses import dataclass


@dataclass
class FilePathsData:
    markdown_file: str = 'data/readme.md'
    en_markdown_file: str = 'data/readme_en.md'
    rus_dict_file: str = 'data/dictionaries/rus.txt'
    en_dict_file: str = 'data/dictionaries/en.txt'


def get_strip_lines_by_file(file_path) -> Iterator:
    with open(file_path, 'r') as out:
        lines = map(lambda s: s.strip(), out.readlines())

    return lines


def get_text_by_file(file_path):
    with open(file_path, 'r') as out:
        return out.read()


def write_list_to_file(strings_list, file_path):
    with open(file_path, "w") as output:
        for row in strings_list:
            output.write(str(row) + '\n')


def write_text_to_file(text, file_path):
    with open(file_path, "w") as output:
        output.write(text)
