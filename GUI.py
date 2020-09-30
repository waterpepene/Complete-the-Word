import PySimpleGUI as sg

sg.theme("DarkBlue16")
sg.theme_border_width(0)
sg.theme_background_color("#15A2F1")
sg.theme_text_element_background_color(sg.theme_background_color())
sg.theme_input_background_color("#046FED")
sg.theme_button_color(("#3FD1FF", "#2722FA"))

base64_copy_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAALAAAACwARRqq2kAAAIKSURBVFhH7Ze/S0JRFMefgoKKOusgUqG4NgQFLU1BQ0RBtOS/EEFb4BS4udTQFC4NhREVNLUUgVttpUWLgy7izxRFfH3PfSdT/PXqPVx6H7icc67v3Pv13vPwKI1DluVAoVDIwmqmXq9fwAR4aXUgISKydaJSqdzCqBdBD+fz+aNPIFbQhwgvL5nYjgVJpHpLiX5Hu92eMpvN2xxKmUzmzOfzbZLfJwAbhWDCSqSJuMlkeiGHxJdKpRO3271AcTqdfgoGg7Pk90CbNxoNuiPNNJvNGxj6MoJisRhTPpHlVColhBFmtmLzWq12bLVal3lKExaLZQVVf0jr8tRAOgJA2G63L7KvCzabbQlm5HWKGiCVeD0unU5n5/VA4SRQOO8cqgZ5AeStcSjlcrmEx+PZoCtADezQHGrgFTXwczIQEMXoUK1WH2BGHt0wKK9cLj+LhQDe3iJMaGwNdONwOB6/K/i3UB5GkkMJ1+qGGXoNAwVMEkOAIcAQYAgwBPxPAfixktmdnAD0AiV2qVt6Y3eiJ3DaarUO0PjE/H7/Hs9NTgCOPY1vvu9yuXbJ5+nBAtCczqNx+XNHhDHHIa1FRx9Xon66e8Jr9ITTYlbhHONDcdWDnnAGPeE6h1I2m73yer2rHA4HInr6Qh2J8hajwYN0CkklRx/QkN7DqL9Kehh3dieyNcL/sMZsLklfuF4Vs1jRAZUAAAAASUVORK5CYII='
base64_info_icon = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsEAAA7BAbiRa+0AAAKTSURBVFhHxZe9b9RAEMVthwIpRXRCUKWguXwUkSjSQJk6BfRI+Sv4B1KDlD5VUqRIlYIqEmmgJqkoTghRggRCqSiId3lv901Y53xn+7iPn/TOe7OzM/Z6vR7nWUu8d70sy3fR3IGeQI+hFYhcQ1+hK+gCepvn+S8c/x/v/SZ0BP2G2kJfjtlUmO7gipcR4AD6A93lO/QeOpPYpu0uHIsYbllh24FB69AnRkgYQK+gPiTPf9CmPvrQN4Wx1uU6HjhuQz84SnyD9pwrl+TSCH05RmMNxtyWSz1w4JWnyc+hh+qu4LwrMLVPoWfOuULmChyrGAZj18+E7nk67Sew3VP3EOh/Hd0Cb2QegjHQj1i3IEfNmkAHF5xxjiscmZzA5110DXyQuRadRDoTB+qKwMBHzVY771vttKfA5wX0GfrCtswjYUzI1gRzbagrdPKZNfZknjqMHVMEjszYg2yTGbRZ7fCrVRN6OuwRRU7X4+rl9no/eGTZYVEslWpPHcU+jP+YM9/lCXBvN850HAv2efz6ffx8jPL70daKNMcOp+4yzkjYSmVvBtN3HIcRdyxzI3CmbNu+5AzwrUYGHa5iYpRjEP4gN0/AXqk/dZwHlmuldgudJzwBFhPkgY7zwHJd8wRYyZA1LAo1Z4dyrIU/yM0TYBlFHkH92JwpzMFc5IonwBrOeK7jLElzXHBKOm/FZJJ9YHgr9r1C1etpdMn6eV68VHvqKLbd5lPlDgtjgtdxtxmA0+jXMYGhUpAg6NiCpHQ3q6Urt6JuVmWuhbFizFuqBQmBU6eSrC1K3lySEXS2LkrbwLGKYYwuSg04LK4sN+C4uA8TQ2tiMZ9mKQiwAU36cVp91Gro8Hnu8Xke6scpfp5n2V85tHFuhNzWwwAAAABJRU5ErkJggg=='
base64_dictionary = b'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'


def label_and_input(label_text: str, key: str):
    return sg.Text(label_text, font=("Dubai", 23)), \
           sg.InputText("", justification="center", font=("Segoe UI Symbol", 20), key=key, size=(8, 1), pad=((0, 50), 0))

                    # using these two functions to avoid the re-use of the same elements

def row_lbl_and_ib(*name_and_keys):
    row = *label_and_input(name_and_keys[0], name_and_keys[1]), *label_and_input(name_and_keys[2], name_and_keys[3]),\
          *label_and_input(name_and_keys[4], name_and_keys[5])
    return row


window_layout = [[sg.Text("Complete the word!", font=("Segoe UI Semibold", 35)),
                  sg.Button("", image_data=base64_info_icon, key="-INFO-",
                            button_color=(sg.theme_background_color(), sg.theme_background_color()))],

                 [sg.Text("_" * 100 + "\n"*2)],  # horizontal separator

                 [*row_lbl_and_ib("Starts with: ", "-STARTS_WITH-", "Ends with: ",
                                  "-ENDS_WITH-", "Letter Count: ", "-LETTER_COUNT-")],

                 [*label_and_input("Contains the letters: ", "-HAS_LETTERS-")],

                 [sg.Listbox(["   The compatible words will be here."], font=("Segoe UI Symbol", 20), size=(30, 5),
                             pad=(0, 20), enable_events=True, key="-ALL_WORDS-", select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)],

                 [sg.Text(" "*10),
                  sg.InputText("", font=("Segoe UI Symbol", 20), justification="c", key="-CHOSEN_WORD-", size=(20, 1)),

                  sg.Button("", image_data=base64_copy_icon, key="-COPY-", tooltip="Copy the word to your clipboard",
                            button_color=(sg.theme_background_color(), sg.theme_background_color())),

                  sg.Button("", image_data=base64_dictionary, key="-DICTIONARY-", tooltip="Search the word in the dictionary",
                            button_color=(sg.theme_background_color(), sg.theme_background_color()))],

                 [sg.Text("\n" * 2 + "_" * 100 + "\n" * 3)],  # horizontal separator

                 [sg.Button("Reset", key="-RESET_VALUES-", font=("Segoe UI Symbol", 16), auto_size_button=True),
                  sg.Button("Search!", key="-SEARCH-", font=("Segoe UI Symbol", 16), auto_size_button=True,
                            tooltip="Search for words matching the above specifications.")]]


window = sg.Window("Complete the word",
                   window_layout,
                   element_justification="center",
                   size=(1280, 720),
                   resizable=True,
                   text_justification="center",
                   finalize=True)


def info_window():
    sg.theme("DarkBlue16")

    info_window_layout = [[sg.Text("Word Completer", font=("Segoe UI Symbol", 24))],
                          [sg.Text("This app is used to find words that match the given specifications.\n"
                                   "If a given word is clicked, it will appear below the List Box where \n"
                                   "there will be two buttons which will copy the word to the clipboard\n"
                                   "and the other will open the dictionary definition in the browser.\n"
                                   "_______________________________________________________________________",
                                   font=("Segoe UI Symbol", 16),
                                   justification="center")]]

    infoWindow = sg.Window("Information",
                           info_window_layout,
                           grab_anywhere=True,
                           element_justification="center")
    while True:
        Ievents, Ivalues = infoWindow.Read()

        if Ievents == sg.WIN_CLOSED:
            break

