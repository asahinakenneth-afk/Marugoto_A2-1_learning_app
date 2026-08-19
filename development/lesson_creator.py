from pathlib import Path
import json

'''  Similar to glossary_insert.py, I made this to help people insert the lessons in the program!
    I wish it had an interface... but anyways, to start it's very good... I think?
'''

BASE_DIR = Path(__file__).resolve().parent ## just to make sure...
run = True

while run:

    print("Make sure you aren't trying to add a pre-existing lesson" \
          "or all the information WILL be lost (rewritten)!")
    new_lesson = input("Do you want to add a new lesson? (Y/N)").lower()

    while new_lesson == "y":
        n = int(input("Enter the number of the lesson: "))

        ''' We create the paths and files for the lessons first...'''

        path = BASE_DIR / ".." / "data" / "content" / "lessons" / f"lesson_{n}" ## the path (if it doesnt exist yet)

        path.mkdir(parents=True, exist_ok=True)

        # We create the template files...
        vocabulary = path / "vocabulary.json"
        lesson = path / "lesson.json"
        test = path / "test.json"

        vocabulary.touch(exist_ok=True)
        vocabulary.write_text('''{
        "words" : {
        },
        "verbs" : {
        },
        "adjectives" : {
        }
        }''')
        lesson.touch(exist_ok=True)
        test.touch(exist_ok=True)

        '''     VOCABULARY PHASE    '''

        print(f"""Please have your words ready :3!
        1. In the case of verbs, you only need to refer to their number ID in glossary.json
        same with adjectives!
        2. You need to type the word type this way: 
        - Noun  --> n
        - Verb  --> v
        - Adjectives    --> adj
        - Adverbs   --> adv
        - Suffix    --> s
        - Prefixes  --> p""")

        with open(vocabulary, "r", encoding='utf-8') as archivo:
            vocabulary_file = json.load(archivo)
        with open('data/local/config.json', 'r', encoding='utf-8') as archivo:
            config_file = json.load(archivo)
            language = config_file.get("language", "en")

        vocabulary_phase = True

        while vocabulary_phase:

            type = input("Which word type?: ").lower()

            if type == "v":
                id = str(input("Insert the ID of the verb: "))
                vocabulary_file["verbs"][f"v_{id}"] = id

                with open(vocabulary, 'w', encoding='utf-8') as archivo:
                    json.dump(vocabulary_file, archivo, ensure_ascii=False, indent=4)
            elif type == "adj":
                id = str(input("Insert the ID of the adjective: "))
                vocabulary_file["adjectives"][f"adj_{id}"] = id

                with open(vocabulary, 'w', encoding='utf-8') as archivo:
                    json.dump(vocabulary_file, archivo, ensure_ascii=False, indent=4)   

            elif type == "n" or type == "adv" or type == "s" or type == "p" :
                kanji = input("Insert the kanji version of the word: ")
                kana = input("Insert the kana reading of the word: ")
                key = len(vocabulary_file["words"]) + 1
                vocabulary_file["words"][f"w_{key}"] = {
                    "kanji" : kanji,
                    "kana" : kana,
                    "type" : type
                }
                with open(vocabulary, 'w', encoding='utf-8') as archivo:
                    json.dump(vocabulary_file, archivo, ensure_ascii=False, indent=4)
            else:
                print(f'''There has been an unexpected error, try to
                - Determine if you've wrote the type properly (as said above)''')

            repeat = input("Do you wish to add another word? (y/n)").lower()
            if repeat == "y":
                vocabulary_phase = True
            else: 
                vocabulary_phase = False

            ''' LESSON PHASE '''

            '''  TEST PHASE  '''