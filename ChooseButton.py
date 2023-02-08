# 导入库
import PySimpleGUI as sg

a =['python','java','c++','php','html']
# 定义布局，确定行数
layout = [
    [sg.T('OptionMeNU'),sg.OptionMenu(a,key='-OM-'),
    sg.T('Spin'),sg.Spin(a,key='-SP-',enable_events=True)],
    [sg.T('语言'),sg.In(key='-YY-',size=(25))]
    ]

# 创建窗口
window = sg.Window('演示弹窗',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '-SP-':
        window['-YY-'].update(values['-SP-'])

# 关闭窗口
window.close()