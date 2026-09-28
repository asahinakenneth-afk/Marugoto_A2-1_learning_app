

'''
    This is for the pop-ups in the app, to save up resources and optimize, I've seen it would be 
    better to separate the lessons from the tests and the dictionary, but they're all here, what changes
    is what is being executed, and what isn't
    The trick is that the code only imports the necessary functions (like conjugations and
    dictionary) only when the part of the app that needs it is executed
    It's promising to take less time to executate the program itself and consume less RAM
    We use QDialog for this :)
'''