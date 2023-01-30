# 导入库
import PySimpleGUI as sg

# 主题
sg.theme('GrayGrayGray')

# 定义布局，确定行数
layout =[
    [sg.Text('请输入您的信息')],
    [sg.Text('姓名'),sg.InputText('派大星')],
    [sg.Text('性别'),sg.InputText('男')],
    [sg.Text('国籍'),sg.InputText('中国')],
    [sg.Button('确定'),sg.Button('取消')]
]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '确定':
        sg.Popup('您已确定！')
    if event == '取消':
        sg.Popup('您已取消！')

# 关闭窗口
window.close()
