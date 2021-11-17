# Markdown translater

Translating in two step:
1. For creating rus dictionary from initial file
   1. Run `python3 dict_creator.py --type=markdown` for markdown files
   1. Run `python3 dict_creator.py` for other file types 
1. Run `python3 replacer.py` - for creating new markdown file with replaced not latin idioms