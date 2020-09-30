from re import search
from itertools import islice

# this dictionary contains the starting line of each letter in the 'all words.txt' file.
alphabet_index = {"a": 1,      "b": 25417,  "c": 43830,  "d": 75937,  "e": 94670,  "f": 108867, "g": 120760, "h": 131713,
                  "i": 145456, "j": 159798, "k": 162638, "l": 166590, "m": 176592, "n": 196397, "o": 209855, "p": 222536,
                  "q": 257396, "r": 259189, "s": 275972, "t": 314736, "u": 333555, "v": 356322, "w": 361651, "x": 368210,
                  "z": 368717}
alphabet_index_list = list(alphabet_index)


def return_expression(starting="", letter_count=0, ends_with="", contains_letters=""):
    """
    This function returns a regex expression that will be used to match a word with the above parameters.
    """
    contains = ""

    """ storing the lengths of 'starting' and 'contains_letters' in a list and then subtracting them by 'letter_count'
        to get the total number of letters after 'starting' and 'contains_letters' had been used in the regex.
        i did this because to match a word to a number of letters i had to use .{length_to_count} after both 
        'starting' and 'contains_letters'."""
    if letter_count is not 0:
        lengths = [starting.__len__() if starting is not "" else 1,
                   ends_with.__len__() if ends_with is not "" else 1,
                   len(contains_letters) if contains_letters is not "" else 0]

        try:
            length_for_count = letter_count - sum(lengths)
        except TypeError:   # pass if there is no 'letter_count' parameter
            length_for_count = None
    else:
        letter_count = None

    try:
        for letter in contains_letters:             # positive lookahead for every letter in 'contains_letters'
            contains = contains + f"(?=.*{letter})"
            if length_for_count is not None: length_for_count += 1

    except TypeError:   # pass if there is no 'contains_letters' parameter
        pass

    expression_list = [f"^({starting})" if starting is not "" else f"^[a-z]",
                       contains if contains_letters is not None else "",
                       f".{{{length_for_count}}}" if letter_count is not None else ".*",
                       f"({ends_with})$" if ends_with is not "" else "[a-z]$"]

    try:        # getting the value of the letter that comes after the starting letter.
        next_starting_letter = alphabet_index[alphabet_index_list[alphabet_index_list.index(starting[0]) + 1]]
    except (ValueError, IndexError):
        next_starting_letter = 370103   # last line in 'all words.txt'

    # returns the regex expression, line number for the first character in 'starting' parameter and the line number of
    # the next key in 'alphabet_index'
    try:
        return r"".join(expression_list), alphabet_index[starting[0]], next_starting_letter

    # return regex expression, first and last line in the 'all words.txt' file if parameter 'starting' is None
    except IndexError:
        return r"".join(expression_list), 1, next_starting_letter


def get_compatible_words(expression):
    compatible_words = []
    print(expression)

    with open("all words.txt", "r") as f:
        for word in islice(f, expression[1], expression[2]):
            if search(expression[0], word):
                compatible_words.append(str(word).replace("\n", "").center(55))
    return compatible_words

