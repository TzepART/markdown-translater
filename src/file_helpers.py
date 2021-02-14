from collections import Iterator


def get_strip_lines_by_file(file_path) -> Iterator:
    with open(file_path, 'r') as out:
        lines = map(lambda s: s.strip(), out.readlines())

    return lines
