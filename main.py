import json
import os

import PySimpleGUI as sg

# JSON example of what i want

# x = {
#   "name": "Kahlid",
#   "age": 30,
#   "protag": True,
#   "main": True,
#   "Species": ("NonHu","Demon"),
#   "skillset": [Muay Thai, Wrestling],
#   "appearance": [
#     {"book1": ("Part1", "part2", "part3")},
#     {"book2": ("Part1", "part2", "part3")},
#     {"book3": ("Part3", "Part4", "Part5")}
#   ]
# }
pronouns = 'She/Her', 'He/Him', 'They/Them'
directory = "Character_Sheet"
parent_dir = "E:\Practice\character_sheet_holder"
path = os.path.join(parent_dir, directory)

if os.path.isdir(directory):
    pass
else:
    os.mkdir(directory)


# title = 'Customized Titlebar Window'
# Here the titlebar colors are based on the theme. A few suggestions are shown. Try each of them
# layout = [title_bar(title, sg.theme_button_color()[0], sg.theme_button_color()[1])]
def array_string(str):
    date = ""
    for str2 in str:
        date += str2

        return date


def profile():
    sg.theme('DarkAmber')
    layout = [[sg.Text("Enter Character Name"), sg.I('', size=(18, 1), key='NAME')],
              [sg.Text("Enter Age"), sg.I('', size=(6, 1), key="AGE")],
              [sg.Text("Preferred Pronouns"),
               sg.Combo(values=('She/Her', 'He/Him', 'They/Them'), key="PRONOUNS")],
              # Key is basically its variable Name
              [sg.Radio("Main Character", "char-imp", k='MAIN', default=False),
               sg.Radio("Side Character", "char-imp", k='SIDE', default=False)],
              # Separate line to determine if Villain or not.
              [sg.Checkbox("Antagonist", default=False, k='HERO')],
              [sg.Text("Enter Birthday"), sg.I('', size=(3, 1), key='MONTH'), sg.T('/'),
               sg.I('', size=(3, 1), key='DAY'), sg.T('/'), sg.I('', size=(5, 1), key='YEAR')],
              [sg.Text("Enter a short description of your character"),
               sg.Multiline(size=(25, 3), key='SUMMARY')],
              [sg.B('Submit'), sg.B('Exit')]]

    window = sg.Window('Character Sheet', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        elif event == 'Submit':
            name = values['NAME']
            age = values['AGE']
            pn = values['PRONOUNS']
            main = str(values['MAIN'])
            side = str(values['SIDE'])
            hero = str(values['HERO'])
            birthday = values['MONTH'], values['DAY'], values['YEAR']
            summary = values['SUMMARY']

            layout2 = [[sg.T("Name: " + name)],
                       [sg.T("Age:" + age)],
                       [sg.T("Pronouns: " + pn)],
                       [sg.T("Main Character: " + main)],
                       [sg.T("Side Character: " + side)],
                       [sg.T("Antagonist: " + hero)],
                       [sg.T("Birthday: " + array_string(birthday))],
                       [sg.T("Summary: " + summary)],
                       [sg.T('CONSOLE: ')],
                       [sg.B("Submit")]
                       ]
            window2 = sg.Window("Results", layout2)
            while True:
                event1, values1 = window2.read()
                if event1 == sg.WIN_CLOSED:
                    break
                elif event1 == 'Submit':
                    character = {"NAME": name,
                                 "AGE": age,
                                 "PRONOUNS": pn,
                                 "MAIN": main,
                                 "SIDE": side,
                                 "ANTAGONIST": hero,
                                 "BIRTHDAY": array_string(birthday),
                                 "SUMMARY": summary}
                    file_name = name + ".json"
                    char_raw = os.path.join(directory, file_name)
                    char_file = open(char_raw, "w")
                    char_json = json.dumps(character, indent=5)

                    char_file.write(char_json)
                    char_file.close()
                    print(char_json)

    window.close()


profile()
