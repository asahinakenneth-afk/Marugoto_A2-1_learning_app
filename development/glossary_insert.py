import json

'''
    For now, it's a simple terminal, but it helps a LOT when it comes to not copy-pastying
    over and over in the glossary file... I hope it helps, developers!
'''

with open("data/content/glossary.json", 'r', encoding='utf-8') as archivo:
    glossary_file = json.load(archivo)

with open("data/local/config.json", 'r', encoding='utf-8') as archivo:
    config_file = json.load(archivo)
    language = config_file.get("language", "en")

with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
    language_file = json.load(archivo)

run = True

while True:
    print(f"""Greetings to the inserting tool for the glossary file!
    You just need to insert the following information:
    1. The verb in dictionary stem (Specifically use kanji)
    2. The kana/reading of the kanji in the verb (飲・む -> の)
    3. The group of the verb (1 or 2, the only 3 group verbs are already inserted
    4. The masu stem of the verb (飲・む -> 飲みます)
    5. The translation of the verb in {language} (language in your config file
    But if you wish, you can also add the translation to other languages)
    """)
