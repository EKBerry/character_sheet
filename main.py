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
directory = "Character_Sheet"
parent_dir = "E:\Practice\character_sheet_holder"
path = os.path.join(parent_dir, directory)

if os.path.isdir(directory):
    pass
else:
    os.mkdir(directory)

# Loading the Pronouns file  while putting the file's data in a variable.
pn_file = open("Character_Sheet/pronouns.txt", "r")
pn_data = pn_file.readlines()

# List to be used in the program itself later
pn_list = []

# Removing the Newline in the data in placing the new data into a list to be used
for x in range(len(pn_data)):
    pn_list.append(pn_data[x].replace('\n', ''))
print(pn_list)


# Transform Arrays into a string
def array_string(var):
    str1 = " "
    return str1.join(var)


# The Main Profile Maker
def profile():
    sg.theme('DarkAmber')
    new_profile = [[sg.Text("Enter Character Name:"), sg.I('', size=(18, 1), key='-NAME-')],
                   [sg.T("Enter Height *in CM*:"), sg.I('', size=(6, 1), key="-HEIGHT-"),
                    sg.T("Enter Weight:"), sg.I('', size=(6, 1), key='-WEIGHT-')],
                   [sg.Text("Enter Age:"), sg.I('', size=(6, 1), key="-AGE-"),
                    sg.Text("Enter Birthday:"), sg.I('', size=(3, 1), key='-MONTH-'), sg.T('/'),
                    sg.I('', size=(3, 1), key='-DAY-'), sg.T('/'), sg.I('', size=(5, 1), key='-YEAR-')],
                   [sg.Text("Preferred Pronouns:"),
                    sg.Combo(pn_list, size=(10, 0), key="-PRONOUNS-"), sg.B("Add")],
                   [sg.Text("Role: "), sg.Combo(values=('Main Character', 'Side Character'), k="-ROLE-"),
                    sg.T("Skills: "), sg.B("Skills")],
                   [sg.Text("Enter a short description of your character: "),
                    sg.Multiline(size=(25, 3), key='-SUMMARY-')],
                   [sg.B('Submit'), sg.B("Clear"), sg.B("Open Character"), sg.B('Exit')]]

    window = sg.Window('Character Sheet', new_profile)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks cancel
            break
        # Add Pronouns Button. Adds Pronouns to the TXT file to later be used.
        elif event == "Add":
            add_layout = [[sg.I('', size=(5, 2), key="-NPN-"), sg.T("/"), sg.I('', size=(5, 2), key="-NPN1-")],
                          [sg.B("Add"), sg.B("Exit")]]

            add_window = sg.Window('Additional', add_layout)
            while True:
                add_event, values = add_window.read()
                if add_event == sg.WIN_CLOSED or add_event == 'Exit':  # if user closes window or clicks cancel
                    break
                elif event == "Add":
                    pnf = open("Character_Sheet/pronouns.txt", "a+")
                    np = values['-NPN-'] + "/" + values['-NPN1-']
                    pnf.write("\n" + np.upper())
                    pnf.close()
                    sg.popup("Pronoun added!")
        # Clears the input areas to make a new profile faster.
        elif event == "Clear":
            for i in values:
                window[i].update('')

        # Opens a saved character and places data into the input boxes
        elif event == 'Open Character':

            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            f = open(folder_or_file)
            data = json.load(f)

            window['-NAME-'].update(data['NAME'])
            window['-AGE-'].update(data['AGE'])
            window['-PRONOUNS-'].update(data['PRONOUNS'])
            window['-HEIGHT-'].update(data['HEIGHT'])
            window['-WEIGHT-'].update(data['WEIGHT'])
            window['-ROLE-'].update(data['ROLE'])
            birth_arr = data['BIRTHDAY'].split()
            month = birth_arr[0]
            day = birth_arr[2]
            year = birth_arr[4]

            window['-MONTH-'].update(month)
            window['-DAY-'].update(day)
            window['-YEAR-'].update(year)
            window['-SUMMARY-'].update(data['SUMMARY'])
        # Shows a box with the data, saves the profile (if new) and updates existing profiles.
        elif event == 'Submit':
            name = values['-NAME-']
            age = values['-AGE-']
            height = values['-HEIGHT-']
            weight = values['-WEIGHT-']
            pn = values['-PRONOUNS-']
            role = str(values['-ROLE-'])
            bdraw = values['-MONTH-'], "-", values['-DAY-'], "-", values['-YEAR-']
            summary = values['-SUMMARY-']
            birthday = array_string(bdraw)
            skills = ''
            print_layout = [[sg.T("NAME: " + name)],
                            [sg.T("AGE:" + age)],
                            [sg.T("HEIGHT:" + height)],
                            [sg.T("WEIGHT:" + weight)],
                            [sg.T("PRONOUNS: " + pn)],
                            [sg.T("CHARACTER ROLE: " + role)],
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
                                 "HEIGHT": height,
                                 "WEIGHT": weight,
                                 "PRONOUNS": pn,
                                 "ROLE": role,
                                 "BIRTHDAY": birthday,
                                 "SUMMARY": summary}
                    file_name = name + ".json"
                    char_raw = os.path.join(directory, file_name)
                    char_file = open(char_raw, "w")
                    char_json = json.dumps(character, indent=5)

                    char_file.write(char_json)
                    char_file.close()
                    print(char_json)

        elif event == 'Skills':
            skill_file = open("Character_Sheet/skills.txt", "r")
            skill_data = skill_file.readlines()
            skill_list = []

            for y in range(len(skill_data)):
                skill_list += skill_data[y].replace('\n', '')
            skill_layout = [[sg.Checkbox(skill_list)]]
            skill_window = sg.Window('Skill Mark', skill_layout)
            while True:
                skill_event, skill_values = skill_window.read()
                if skill_event == sg.WIN_CLOSED:
                    break
                elif skill_event == 'Submit':
                    



    window.close()


profile()
