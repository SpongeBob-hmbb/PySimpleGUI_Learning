# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.CB('1'),sg.CB('2')]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break

# 关闭窗口
window.close()