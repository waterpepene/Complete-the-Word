from GUI import *
from functions import *
from pyperclip import copy
from webbrowser import open
"""
 -STARTS_WITH-    -LETTER_COUNT-    -ENDS_WITH-   -HAS_LETTERS-      -CHOSEN_WORD-      -ALL_WORDS-      -SEARCH-    
 -RESET_VALUES-   -DICTIONARY-      -COPY-        -INFO-
"""
while True:
    events, values = window.read()
    chosen_word = values["-CHOSEN_WORD-"]

    if events in "-SEARCH-":
        print(values)
        words = get_compatible_words(return_expression(values["-STARTS_WITH-"], int(values["-LETTER_COUNT-"]),
                                                       values["-ENDS_WITH-"], values["-HAS_LETTERS-"]))
        window["-ALL_WORDS-"].update(words)

    if events in "-ALL_WORDS-":
        window["-CHOSEN_WORD-"].update(values["-ALL_WORDS-"][0].strip())

    if events == "-RESET_VALUES-":
        window["-STARTS_WITH-"].update("")
        window["-LETTER_COUNT-"].update("")
        window["-ENDS_WITH-"].update("")
        window["-HAS_LETTERS-"].update("")
        window["-CHOSEN_WORD-"].update("")
        window["-ALL_WORDS-"].update(values=["   The compatible words will be here."])

    if events in "-COPY-":
        copy(chosen_word)

    if events in "-DICTIONARY-":
        open(f"https://www.dictionary.com/browse/{chosen_word}?s=t")

    if events in "-INFO-":
        info_window()