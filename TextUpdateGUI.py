# 导入库
from tkinter import E
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.T('派大星',key='-Text-'),sg.B('点赞')]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()
    print(event)
    if event == None:
        break
    if event == '点赞':
        window['-Text-'].Update(
            value = '谢谢支持！', # str更新文本
            background_color = 'white', # 更新文本背景颜色
            text_color = 'black', # 更新文本颜色
            font = ('黑体',30), # 更新字体的名称或者大小
            visible = None # 更新元素的可见状态
        )

# 关闭窗口
window.close()