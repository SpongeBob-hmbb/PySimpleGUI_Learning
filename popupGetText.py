import PySimpleGUI as sg

# 常用于登录
pwd = '123'
list = ['python','java','php']
while True:
    result = sg.PopupGetText('密码输入框')
    if result == pwd:
        break
    elif result == None:
        exit()
    else:
        sg.popup('输入有误')

layout = [
    [sg.LB(list,size=(30,5))]
]
window = sg.Window('资料查询',layout)
while True:
    event,values = window.read()
    if event == None:
        break

window.close