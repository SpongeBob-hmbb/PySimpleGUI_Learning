# 导入库
import PySimpleGUI as sg

list1 = ['python','java','c++','php','html']
list2 = ['小明','小李','小红','美丽']
# 定义布局，确定行数
layout = [
    [sg.LB(list1,size=(30,2),key = '-list-')],
    [sg.B('编程语言'),sg.B('程序员')],
    [sg.B('set_to_index'),sg.B('scroll_to_index')]
]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()
    print(event)
    key = '-list-'
    if event == None:
        break
    if event == '程序员':
        window[key].update(values = list2)
    if event == '编程语言':
        window[key].update(values = list1)
    if event == 'set_to_index':
        window[key].update(set_to_index=2)#高亮显示
        # print(values[key])
        print(window[key].get()) # 直接被选中的值
    if event == 'scroll_to_index':
        window[key].update(scroll_to_index=2)#滚动到第几行

# 关闭窗口
window.close()