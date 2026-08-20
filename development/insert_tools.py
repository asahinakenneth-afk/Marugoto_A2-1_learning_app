import json

'''
    For now, it's a simple terminal, but it helps a LOT when it comes to not copy-pastying
    over and over in the files... I hope it helps, developers!
'''

def insert_verb(language, language_file):
    with open("data/content/verbs.json", 'r', encoding='utf-8') as archivo:
        verbs_file = json.load(archivo)

    verb_inserting = True
    while verb_inserting:
        print(f"""Greetings to the inserting tool for the verbs file!
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
        
        id = str(len(verbs_file) + 1)
        
        verbs_file[id] = {
            "dict": kanji,
            "kana": kana,
            "group": int(group),
            "masu": masu
        }
        with open("data/content/verbs.json", 'w', encoding='utf-8') as archivo:
                json.dump(verbs_file, archivo, ensure_ascii=False, indent=4)     
        language_file["verbs"][id] = translation
        with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4)
        
        print(f"Verb inserted successfully with ID {id}.")
        
        print("Do you wish to translate it to another language? (y/n)")
        translate = input().lower()
        
        while translate == "y":
            language = input("Insert the language code (e.g., 'es' for Spanish, 'en' for English): ")
        
            translation = input(f"Insert the translation of the verb in {language}: ")
            with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
                language_file = json.load(archivo)
        
            language_file["verbs"][id] = translation
        
            with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4) ## IF YOU DONT PUT THIS IT'S GONNA TURN INTO A DISASTER---
        
            print(f"Translation in {language} inserted successfully!")
        
            print("Do you wish to translate it to another language? (y/n)")
            translate = input().lower()
        
        print("Do you wish to insert another verb? (y/n)")
        verb_inserting = True if input().lower() == "y" else False

def insert_adj(language, language_file):
    with open("data/content/adjectives.json", 'r', encoding='utf-8') as archivo:
        adj_file = json.load(archivo)
        
    adj_inserting = True
    while adj_inserting:
        print(f"""Greetings to the inserting tool for the verbs file!
            You just need to insert the following information:
            1. The verb in dictionary stem (Specifically use kanji)
            2. The kana/reading of the kanji in the verb (飲・む -> の)
            3. The group of the verb in NUMBER (1 or 2, the only 3 group verbs are already inserted)
            4. The masu stem of the verb (飲・む -> 飲みます)
            5. The translation of the verb in {language} (language in your config file
            But if you wish, you can also add the translation to other languages)
            """)
        
        kanji = input("Insert the adjective (kanji): ")
        kana = input("Insert the reading of the kanji (kana): ")
        group = input("Insert the group of the adjective (na or i): ")
        translation = input(f"Insert the translation of the verb in {language}: ")
        
        id = str(len(adj_file) + 1)
        
        adj_file[id] = {
            "dict": kanji,
            "kana": kana,
            "group": group,
        }
        with open("data/content/adjectives.json", 'w', encoding='utf-8') as archivo:
                json.dump(adj_file, archivo, ensure_ascii=False, indent=4)
        
        language_file["adjectives"][id] = translation
        with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4)
        
        print(f"Verb inserted successfully with ID {id}.")
        
        print("Do you wish to translate it to another language? (y/n)")
        translate = input().lower()
        
        while translate == "y":
            language = input("Insert the language code (e.g., 'es' for Spanish, 'en' for English): ")
    
            translation = input(f"Insert the translation of the verb in {language}: ")

            with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
                language_file = json.load(archivo)
        
            language_file["adjectives"][id] = translation
        
            with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4) ## IF YOU DONT PUT THIS (indent=4) IT'S GONNA TURN INTO A DISASTER---
        
            print(f"Translation in {language} inserted successfully!")
        
            print("Do you wish to translate it to another language? (y/n)")
            translate = input().lower()
        
        print("Do you wish to insert another verb? (y/n)")
        verb_inserting = True if input().lower() == "y" else False

with open("data/local/config.json", 'r', encoding='utf-8') as archivo:
    config_file = json.load(archivo)
    language = config_file.get("language", "en")

with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
    language_file = json.load(archivo)

run = True

while run:
    print(f'''
Select which insertion tool you want to use:
1- Verb insertion tool
2- Adjective insertion tool
3- particles insertion tool
0- exit
''')
    select = str(input())

    while select != "0":
        if select == "1":
            insert_verb(language, language_file)
            select = str(input("Want to add something else? (2,3)"))
        if select == "2":
            insert_adj(language, language_file)
            select = str(input("Want to add something else? (1,3)"))
    run = False