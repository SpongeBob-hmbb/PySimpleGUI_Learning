# 导入库
import PySimpleGUI as sg

dict = {'小明':'python','小李':'java','小红':'php','美丽':'c++'}
list = []

for i in dict:
    list.append(i)
    # print(list)


# 定义布局，确定行数
layout = [
    [sg.Combo(list,key='-LB-',size=(30,6),enable_events=True)],
    [sg.T('语言'),sg.In(key='-YY-',size=(25))]
]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '-LB-':
        window['-YY-'].update(dict[values['-LB-']])
# 关闭窗口
window.close()