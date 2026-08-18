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

while run:
    print(f"""Greetings to the inserting tool for the glossary file!
    You just need to insert the following information:
    1. The verb in dictionary stem (Specifically use kanji)
    2. The kana/reading of the kanji in the verb (飲・む -> の)
    3. The group of the verb in NUMBER (1 or 2, the only 3 group verbs are already inserted)
    4. The masu stem of the verb (飲・む -> 飲みます)
    5. The translation of the verb in {language} (language in your config file
    But if you wish, you can also add the translation to other languages)
    """)

    kanji = input("Insert the verb in dictionary form (kanji): ")
    kana = input("Insert the reading of the kanji (kana): ")
    group = input("Insert the group of the verb (1/Godan or 2/Ichidan): ")
    masu = input("Insert the masu form of the verb: ")
    translation = input(f"Insert the translation of the verb in {language}: ")

    n = len(glossary_file) + 1

    glossary_file[str(n)] = {
        "dict": kanji,
        "kana": kana,
        "group": int(group),
        "masu": masu
    }

    language_file["verbs"][str(n)] = translation

    with open("data/content/glossary.json", 'w', encoding='utf-8') as archivo:
        json.dump(glossary_file, archivo, ensure_ascii=False, indent=4)

    with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
        json.dump(language_file, archivo, ensure_ascii=False, indent=4)

    print(f"Verb inserted successfully with ID {n}.")

    print("Do you wish to translate it to another language? (y/n)")
    translate = input().lower()

    while translate == "y":
        language = input("Insert the language code (e.g., 'es' for Spanish, 'en' for English): ")

        translation = input(f"Insert the translation of the verb in {language}: ")
        with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
            language_file = json.load(archivo)

        language_file["verbs"][str(n)] = translation

        with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
            json.dump(language_file, archivo, ensure_ascii=False, indent=4) ## IF YOU DONT PUT THIS IT'S GONNA TURN INTO A DISASTER---

        print(f"Translation in {language} inserted successfully!")

        print("Do you wish to translate it to another language? (y/n)")
        translate = input().lower()

    print("Do you wish to insert another verb? (y/n)")
    run = True if input().lower() == "y" else False
