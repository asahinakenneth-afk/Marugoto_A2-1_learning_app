import json
from random import randint

'''To initiate properly, the program checks if a verb can be accessed in the glossary and conjugates it
    and if it can, it returns the verb's information, stem forms and let's the program process normally
    if it can't, it returns an error message and the program stops.
'''

config_file_path = "data/local/config.json" ## CONFIGURATION FILE

with open(config_file_path, 'r', encoding='utf-8') as config_file: ## OPENS IT TO CHECK ON USER PREFERENCES
    config_data = json.load(config_file)
    language = config_data.get("language", "en")  # Default to "english" if not found

glossary_path = "data/content/glossary.json" 
language_path = f"data/local/languages/{language}.json" ## SETS LANGUAGE FOR TRANSLATION

with open(glossary_path, 'r', encoding='utf-8') as file:
    glossary = json.load(file)

with open(language_path, 'r', encoding='utf-8') as file:
    language_data = json.load(file)

print("Basic info loaded successfully. Language:", language, "Glossary entries:", len(glossary))

'''VERB CONJUGATION FUNCTIONS'''

def get_verb_info(verb_id, glossary, language_data, language):
    '''
    Here you get the information of the verb you want to use, based on the verb_id,
    the dedicated glossary and dynamic language.
    It returns a dictionary with the verb's information (meaning, dict_form, dict_form, romanji, group
    dictionary form, masu form, etc...)
    This is mainly used to display the verb's information in the GUI,
    and also to get the verb's conjugation forms (check verb_to_te function).
    '''
    id = str(verb_id) # INT TO STRING FOR THE DICTIONARY KEY

    if id not in glossary or id not in language_data["verbs"]: ##IT EXISTS IN GLOSSARY AND LANGUAGE?
        print(f"Verb ID {id} not found in glossary for language {language}.")
        return None

    ##IT EXISTS SO WE GET THE INFO
    verb_data = glossary[id]
    verb_meaning = language_data["verbs"][id]
    
    verb_info = {
        "dict_form": verb_data.get("dict"),
        "romaji": verb_data.get("romaji"),
        "group": verb_data.get("group"),
        "masu_form": verb_data.get("masu"),
        "meaning": verb_meaning
    }

    # print(f"""Verb ID found, printing verbs information...
    #      {verb_info}""")

    return verb_info

def verb_to_te(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    and returns the te-form of the verb.
    It uses the verb's group to determine how to conjugate it.
    '''
    verb_info = get_verb_info(verb_id, glossary, language_data, language)
    
    if not verb_info:
        print(f"Cannot conjugate verb ID {verb_id} because it was not found.")
        return None

    group = verb_info["group"]
    dict_form = verb_info["dict_form"]

    if group == 3: #IRREGULAR
        dict_form = verb_info["dict_form"]
        if dict_form == "する":
            te_form = "して"
        elif dict_form == "くる":
            te_form = "来て"
        else:
            print(f"Unexpected irregular verb: {dict_form}")
            return None

    elif group == 2: #ICHIDAN
        te_form = dict_form[:-1] + "て"

    elif group == 1:  #GODAN
        if dict_form == "行く":
            te_form = "行って"
        elif dict_form.endswith("う") or dict_form.endswith("つ") or dict_form.endswith("る"):
            te_form = dict_form[:-1] + "って"
        elif dict_form.endswith("む") or dict_form.endswith("ぶ") or dict_form.endswith("ぬ"):
            te_form = dict_form[:-1] + "んで"
        elif dict_form.endswith("く"):
            te_form = dict_form[:-1] + "いて"
        elif dict_form.endswith("ぐ"):
            te_form = dict_form[:-1] + "いで"
        elif dict_form.endswith("す"):
            te_form = dict_form[:-1] + "して"
        else:
            print(f"Unexpected ending for Godan verb: {dict_form}")
            return None
        
    # print(f"The te-form of {dict_form} ({dict_form}) is: {te_form} ({te_form})")

    return te_form

def verb_to_ta(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    transforms it to te form, then to ta form (or informal past form) of the verb.
    It returns the ta-form of the verb.
    '''
    te_form = verb_to_te(verb_id, glossary, language_data, language)
    
    if not te_form:
        print(f"Cannot conjugate verb ID {verb_id} to ta-form because te-form was not found.")
        return None

    # Convert te-form to ta-form
    if te_form.endswith("て"):
        ta_form = te_form[:-1] + "た"
    elif te_form.endswith("で"):
        ta_form = te_form[:-1] + "だ"
    else:
        print(f"Unexpected ending for te-form: {te_form}")
        return None

    # print(f"The ta-form of {te_form} ({te_form}) is: {dict_form_ta} ({ta_form})")

    return ta_form

def masu_to_past(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    and returns the past form of the verb in masu form.
    It uses the verb's masu form to determine its conjugation.
    '''
    verb_info = get_verb_info(verb_id, glossary, language_data, language)
    
    if not verb_info:
        print(f"Cannot conjugate verb ID {verb_id} because it was not found.")
        return None

    masu = verb_info["masu_form"]

    if masu.endswith("ます"):
        past_masu_form = masu[:-2] + "ました"
    else:
        print(f"Cannot conjugate verb ID {verb_id} because of an unexpected error.")

    return past_masu_form

def verb_to_tai(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    and returns the tai-form of the verb (or to-wish form)
    It uses the verb's masu form to determine its conjugation.
    '''
    verb_info = get_verb_info(verb_id, glossary, language_data, language)
    
    if not verb_info:
        print(f"Cannot conjugate verb ID {verb_id} because it was not found.")
        return None

    masu = verb_info["masu_form"]

    if masu.endswith("ます"):
        tai_form = masu[:-2] + "たい"
    else:
        print(f"Cannot conjugate verb ID {verb_id} because of an unexpected error.")

    return tai_form

'''VERB CONJUGATION TO 
NEGATIVE FORM FUNCTIONS'''

def masu_to_negative(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    and returns the negative form of the verb in masu form.
    It uses the verb's masu form to determine its conjugation.
    '''
    verb_info = get_verb_info(verb_id, glossary, language_data, language)
    
    if not verb_info:
        print(f"Cannot conjugate verb ID {verb_id} because it was not found.")
        return None

    masu = verb_info["masu_form"]

    if masu.endswith("ます"):
        neg_masu_form = masu[:-2] + "ません"
    else:
        print(f"Cannot conjugate verb ID {verb_id} because of an unexpected error.")

    return neg_masu_form

def mashita_to_negative(verb_id, glossary, language_data, language):
    '''
    This function takes a verb_id, the glossary and the language as input,
    and returns the negative form of the verb in past masu form.
    It uses the verb's past masu form to determine its conjugation.
    '''
    verb_info = get_verb_info(verb_id, glossary, language_data, language)
    
    if not verb_info:
        print(f"Cannot conjugate verb ID {verb_id} because it was not found.")
        return None

    past_masu = masu_to_past(verb_id, glossary, language_data, language)

    if past_masu.endswith("ました"):
        negpast_masu_form = past_masu[:-3] + "ませんでした"

    return negpast_masu_form

print("Testing verb conjugation functions...")
n = randint(1, len(glossary))
print(get_verb_info(n, glossary, language_data, language))
print(verb_to_te(n, glossary, language_data, language))
print(verb_to_ta(n, glossary, language_data, language))
print(verb_to_tai(n, glossary, language_data, language))
print(masu_to_negative(n, glossary, language_data, language))
print(masu_to_past(n, glossary, language_data, language))
print(mashita_to_negative(n, glossary, language_data, language))

print("functions.py loaded successfully.")