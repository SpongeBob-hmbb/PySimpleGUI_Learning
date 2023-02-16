# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.Slider(key = '-S-')],
    [sg.B('update')]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    
    if event == 'up':
        window['-S-'].update(
            value = 5,
            range=(None,None),
            disabled = None,
            visible = None
        )
# 关闭窗口
window.close()