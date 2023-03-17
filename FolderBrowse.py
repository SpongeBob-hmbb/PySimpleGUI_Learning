import PySimpleGUI as sg
layout = [
    [sg.FileBrowse(button_text="选择文件"),sg.In()],
    [sg.FolderBrowse(button_text="选择文件夹",target='-K1-'),sg.In(),sg.In(key='-K1-')],
    [sg.FileSaveAs(button_text="另存为",target='-K2-'),sg.In(key='-K2-'),sg.In()]
]
window = sg.Window('演示窗口',layout)
while True:
    event,values = window.read()
    if event == None:
        break
window.close()