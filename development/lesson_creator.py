from pathlib import Path

'''  Similar to glossary_insert.py, I made this to help people insert the lessons in the program!
    I wish it had an interface... but anyways
'''

BASE_DIR = Path(__file__).resolve().parent ## just to make sure...
run = True

while run:

    new_lesson = input("Do you want to add a new lesson? (Y/N)").lower()

    while new_lesson == "y":
        n = int(input("Enter the number of the lesson: "))

        ''' We create the paths and files for the lessons first...'''

        path = BASE_DIR / ".." / "data" / "content" / "lessons" / f"lesson_{n}" ## the path (if it doesnt exist yet)

        path.mkdir(parents=True, exist_ok=True)

        vocabulary = path / "vocabulary.json"
        lesson = path / "lesson.json"
        test = path / "test.json"

        vocabulary.touch(exist_ok=True)
        lesson.touch(exist_ok=True)
        test.touch(exist_ok=True)

        '''     VOCABULARY PHASE    '''

        print("Please have your words ready!" \
        "In the case of verbs, you only need to refer to their number ID in glossary.json")