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
def array_string(date):
    str1 = " "
    return str1.join(date)


def profile():
    sg.theme('DarkAmber')
    new_profile = [[sg.Text("Enter Character Name"), sg.I('', size=(18, 1), key='NAME')],
                   [sg.Text("Enter Age"), sg.I('', size=(6, 1), key="AGE")],
                   [sg.Text("Preferred Pronouns"),
                    sg.Combo(values=('She/Her', 'He/Him', 'They/Them'), key="PRONOUNS")],
                   # Key is basically its variable Name
                   [sg.Checkbox("Main Character", k='MAIN', default=False),
                    sg.Checkbox("Side Character", k='SIDE', default=False)],
                   # Separate line to determine if Villain or not.
                   [sg.Checkbox("Hero", default=True, k='HERO')],
                   [sg.Text("Enter Birthday"), sg.I('', size=(3, 1), key='MONTH'), sg.T('/'),
                    sg.I('', size=(3, 1), key='DAY'), sg.T('/'), sg.I('', size=(5, 1), key='YEAR')],
                   [sg.Text("Enter a short description of your character"),
                    sg.Multiline(size=(25, 3), key='SUMMARY')],
                   [sg.B('Submit'), sg.B("Clear"), sg.B("Open Character"), sg.B('Exit')]]

    window = sg.Window('Character Sheet', new_profile)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        elif event == "Clear":
            for i in values:
                window[i].update('')
                
            print("Window Cleared!")

        elif event == 'Open Character':

            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            f = open(folder_or_file)
            data = json.load(f)
            print(data)
            main_val = data['MAIN']
            side_val = data['SIDE']
            hero_val = data['HERO']

            window['NAME'].update(data['NAME'])
            window['AGE'].update(data['AGE'])
            window['PRONOUNS'].update(data['PRONOUNS'])
            window['MAIN'].update(eval(main_val))
            window['SIDE'].update(eval(side_val))
            window['HERO'].update(eval(hero_val))
            birth_arr = data['BIRTHDAY'].split()
            month = birth_arr[0]
            day = birth_arr[2]
            year = birth_arr[4]

            window['MONTH'].update(month)
            window['DAY'].update(day)
            window['YEAR'].update(year)
            window['SUMMARY'].update(data['SUMMARY'])

        elif event == 'Submit':
            name = values['NAME']
            age = values['AGE']
            pn = values['PRONOUNS']
            main = str(values['MAIN'])
            side = str(values['SIDE'])
            hero = str(values['HERO'])
            bdraw = values['MONTH'], "-", values['DAY'], "-", values['YEAR']
            print(bdraw)
            summary = values['SUMMARY']
            birthday = array_string(bdraw)
            print(birthday)
            print_layout = [[sg.T("NAME: " + name)],
                            [sg.T("AGE:" + age)],
                            [sg.T("PRONOUNS: " + pn)],
                            [sg.T("MAIN CHARACTER: " + main)],
                            [sg.T("SIDE CHARACTER: " + side)],
                            [sg.T("HERO: " + hero)],
                            [sg.T("BIRTHDAY: " + birthday)],
                            [sg.T("SUMMARY: " + summary)],
                            [sg.B("Submit")]
                            ]
            window2 = sg.Window("Results", print_layout)
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
                                 "HERO": hero,
                                 "BIRTHDAY": birthday,
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
