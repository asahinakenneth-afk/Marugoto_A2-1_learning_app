import json
from time import sleep

'''
    For now, it's a simple terminal, but it helps a LOT when it comes to not copy-pastying
    over and over in the files... I hope it helps, developers!
'''

def load_files():
    with open("data/local/config.json", 'r', encoding='utf-8') as archivo:
        config_file = json.load(archivo)
        language = config_file.get("language", "en")

    with open(f"data/local/languages/{language}.json", 'r', encoding='utf-8') as archivo:
        language_file = json.load(archivo)
    return language, language_file

def insert_verb(language, language_file):
    with open("data/content/verbs.json", 'r', encoding='utf-8') as archivo:
        verbs_file = json.load(archivo)
    print(f"""Greetings to the inserting tool for the verbs file!
        You just need to insert the following information:
        1. The verb in dictionary stem (Specifically use kanji)
        2. The kana/reading of the kanji in the verb (飲・む -> の)
        3. The romaji version of the dictionary stem (will be used as an id)
        4. The group of the verb in NUMBER (1 or 2, the only 3rd group verbs are already inserted)
        5. The masu stem of the verb (飲・む -> 飲みます)
        6. The translation of the verb in '{language}' (language in your config file.
        But if you wish, you can also add the translation to other languages)
        """)

    verb_inserting = True
    while verb_inserting:
        
        kanji = input("Insert the verb in dictionary form (kanji): ")
        kana = input("Insert the reading of the kanji (kana): ")
        id = input("The romaji reading of dictionary stem: ")
        group = input("Insert the group of the verb (1 stands for Godan, 2 for Ichidan): ")
        masu = input("Insert the masu form of the verb: ")
        translation = input(f"Insert the translation of the verb in '{language}': ")
        
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
            1. The adjective (use kanji)
            2. the reading of the kanji (kana)
            3. the romaji reading (it will be used for the id)
            4. The group of the adjective (na/i)
            4. The translation of the verb in {language} (language in your config file
            But if you wish, you can also add the translation to other languages)
            """)
        
        kanji = input("Insert the adjective (kanji): ")
        kana = input("Insert the reading of the kanji (kana): ")
        id = input("romaji reading of the adjective (full): ")
        group = input("Insert the group of the adjective (na or i): ")
        translation = input(f"Insert the translation of the adjective in {language}: ")
        
        adj_file[group][id] = {
            "dict": kanji,
            "kana": kana
        }
        with open("data/content/adjectives.json", 'w', encoding='utf-8') as archivo:
                json.dump(adj_file, archivo, ensure_ascii=False, indent=4)
        
        language_file["adjectives"][id] = translation
        with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4)
        
        print(f"adjective inserted successfully with ID {id}.")
        
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
        
        print("Do you wish to insert another adjective? (y/n)")
        adj_inserting = True if input().lower() == "y" else False

def insert_particles(language, language_file):
    with open("data/content/particles.json", 'r', encoding='utf-8') as archivo:
        part_file = json.load(archivo)
        
    part_inserting = True
    while part_inserting:
        print(f"""Greetings to the inserting tool for the particles file!
            You just need to insert the following information:
            1. The particle (it's a kana)
            2. The romaji (it will be used as an id)
            3. Definitions/usage/equivalences for the particle in {language} 
            4. particle_type of the particle: 
            -- case (1)
            -- binding/topic (2)
            -- adverbial (3)
            -- sentence-ending (4) 
            -- conjunctive (5)
            5. example/s of the usage of this in sentence (the particle must be highlited
            inside []. e.g. 学校[に]行きます)
            """)
        
        particle = input("The particle you want to add: ")
        id = input("The romaji reading: ")
        particle_type = input("Please insert the number of the correspondant type of particle [1 to 5]: ")

        match particle_type: ## this structure is very interesting! :D it replaces if/elif/else and optimizes a lot
            case "1": particle_type = "case"
            case "2": particle_type = "binding/topic"
            case "3": particle_type = "adverbial"
            case "4": particle_type = "sentence-ending"
            case "5": particle_type = "conjunctive"
            case _: particle_type = "unknown"

        definition = input(f"usages or equivalences in {language}: ")

        print("Now you will proceed to insert the examples")

        example_dict = dict()
        part_file[id] = {
            "kana" : particle,
            "examples" : {example_dict}
        }
        with open("data/content/particles.json", 'w', encoding='utf-8') as archivo:
                json.dump(part_file, archivo, ensure_ascii=False, indent=4)

        example_inserting = True
        while example_inserting:
            n = len(example_dict)
            example = str(input("Insert the example oration"))
            new_example= {
                f"example_{n}" : example
            }
            example_dict.update(new_example)
            with open("data/content/particles.json", 'w', encoding='utf-8') as archivo:
                json.dump(part_file, archivo, ensure_ascii=False, indent=4)
            example_inserting = True if input("Do you want to add another example for this particle? (y/n)").lower() == "y" else False

        def_inserting = True if input("Do you want to insert the translation for another language? (y/n): ").lower() == "y" else False
        while def_inserting:
            language = input("Insert the keyword for the language you wish (e.g. es for spanish or en for english)")
            definition = input("Insert the definition")
            language_file["particles"][id] = definition

            with open(f"data/local/languages/{language}.json", 'w', encoding='utf-8') as archivo:
                json.dump(language_file, archivo, ensure_ascii=False, indent=4)
                
            def_inserting= True if input("Do you want to add another meaning for other language? (y/n)").lower() == "y" else False

run = True

while run:
    print(f'''
                     888
                     888
                     888
888  888  888 .d88b. 888 .d8888b .d88b. 88888b.d88b.  .d88b.
888  888  888d8P  Y8b888d88P"   d88""88b888 "888 "88bd8P  Y8b
888  888  88888888888888888     888  888888  888  88888888888
Y88b 888 d88PY8b.    888Y88b.   Y88..88P888  888  888Y8b.
 "Y8888888P"  "Y8888 888 "Y8888P "Y88P" 888  888  888 "Y8888
    ''')
    sleep(5)
    print(f'''
Select which insertion tool you want to use:
1- Verb insertion tool
2- Adjective insertion tool
3- particles insertion tool
0- exit
''')
    select = str(input())
    language, language_file = load_files()

    while select != "0":
        if select == "1":
            insert_verb(language, language_file)
            sleep(5)
            select = str(input("Want to add something else? (1-2-3)"))
        if select == "2":
            insert_adj(language, language_file)
            sleep(5)
            select = str(input("Want to add something else? (1-2-3)"))
    run = False