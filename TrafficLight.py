# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.B('绿灯',key='-green-',button_color=('black','green'),size=(20,10))],
    [sg.B('黄灯',key='-yellow-',button_color=('black','yellow'),size=(20,10))],
    [sg.B('红灯',key='-red-',button_color=('black','red'),size=(20,10))]
    ]
# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '-green-':
        window['-green-'].update(button_color=('black','green'))
        window['-yellow-'].update(button_color=('black','grey'))
        window['-red-'].update(button_color=('black','grey'))

    if event == '-yellow-':
        window['-green-'].update(button_color=('black','grey'))
        window['-yellow-'].update(button_color=('black','yellow'))
        window['-red-'].update(button_color=('black','grey'))

    if event == '-red-':
        window['-green-'].update(button_color=('black','grey'))
        window['-yellow-'].update(button_color=('black','grey'))
        window['-red-'].update(button_color=('black','red'))
# 关闭窗口
window.close()