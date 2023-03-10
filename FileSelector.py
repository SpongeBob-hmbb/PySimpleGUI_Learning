import PySimpleGUI as sg
layout = [
    [sg.FileBrowse(#sg.FilesBrowse选择多个文件
    button_text="browse",
    target='-IN-',
    file_types=(('ALL Files','*.png'),),
    initial_folder=r'D:\\vscode'
    ),
     sg.In(key='-IN-')]
]
window = sg.Window('文件选择器',layout)
while True:
    event,values = window.read()
    if event == None:
        break
window.close()