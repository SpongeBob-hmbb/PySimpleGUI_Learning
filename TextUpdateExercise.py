# 导入库
from tkinter import E
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.B('中文',key = '中文'),sg.B('English',key = 'English')],
    [sg.T('请输入基本信息！',key='-Input-')],
    [sg.T('姓名',key='-name-',size=(8,1)),sg.In()],
    [sg.T('性别',key='-sex-',size=(8,1)),sg.In()],
    [sg.T('国籍',key='-nationality-',size=(8,1)),sg.In()],
    [sg.B('确定',key='-confirm-',size=(8,1)),sg.B('取消',key='-cancel-')]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()
    print(event)
    if event == None:
        break
    if event == 'English':
        window['-Input-'].Update('Please enter basic information')
        window['-name-'].Update('Name')
        window['-sex-'].Update('Sex')
        window['-nationality-'].Update('Nationality')
        window['-confirm-'].Update('Confirm')
        window['-cancel-'].Update('Cancel')

    if event == '中文':
        window['-Input-'].Update('请输入基本信息')
        window['-name-'].Update('姓名')
        window['-sex-'].Update('性别')
        window['-nationality-'].Update('国籍')
        window['-confirm-'].Update('确认')
        window['-cancel-'].Update('取消')

# 关闭窗口
window.close()