import PySimpleGUI as sg
from helper import autogen


# GUI Definition

layout = [
    [sg.Text("Names List:"), sg.Input(key="-IN-"), sg.FileBrowse(file_types = (("Text Files", "*.txt"),))],
    [sg.Text("Template Link:"), sg.Input(key="Link")],
    [sg.Exit(), sg.Button("SUBMIT")]
]

window = sg.Window("Automatic Certificates Generator", layout)

while True:
    event, values = window.read()
    print (event, values)
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "SUBMIT":
        autogen(values["-IN-"], values["Link"])

window.close()