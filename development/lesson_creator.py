from pathlib import Path
import json

'''  Similar to insert_tools.py, I made this to help people insert the lessons in the program!
    I wish it had an interface... but anyways, to start it's very good... I think?
'''

def create_files(vocabulary, lesson, test):
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
    lesson.write_text('''{
        "title" : 
        "kanji" : {
        }
        "grammar" : {
        }
        "conversations" : {
        }
        "Readings" : {
        }
        "Writting" : {
        "Questions" : {

        }

        }
        }''')
    test.touch(exist_ok=True)

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

        create_files(vocabulary, lesson, test)

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
                key = len(vocabulary_file["verbs"]) + 1 
                vocabulary_file["verbs"][f"v_{key}"] = id

                with open(vocabulary, 'w', encoding='utf-8') as archivo:
                    json.dump(vocabulary_file, archivo, ensure_ascii=False, indent=4)

            elif type == "adj":
                id = str(input("Insert the ID of the adjective: "))
                key = len(vocabulary_file["adjectives"]) + 1
                vocabulary_file["adjectives"][f"adj_{key}"] = id

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

            vocabulary_phase = True if input("Do you wish to add another word? (y/n)").lower() == "y" else False

        ''' LESSON PHASE '''

        lesson_phase = True

        while lesson_phase:
            break

        '''  TEST PHASE  '''