# 导入库
import PySimpleGUI as sg

lista = ['非常满意','满意','一般','不满意']
listb = ['请评价内容','请评价讲解']

# 定义布局，确定行数
# layout = [
#     [sg.T('1.'+listb[0])],
#     [sg.R(i,group_id=1)for i in lista],
#     [sg.T('2.'+listb[1])],
#     [sg.R(i,group_id=1)for i in lista]
#     ]
# layout =[[sg.T('1.'+listb[0])]]+\
#         [[sg.R(i,group_id=1)for i in lista]]+\
#         [[sg.T('2.'+listb[1])]]+\
#         [[sg.R(i,group_id=1)for i in lista]]
# layout=[
#     [[sg.R(i,group_id=1)]for i in lista]
# ]
layout=[
    [sg.T(str(y+1))]+[sg.R(x,group_id=y,key=(x,y))for x in lista] for y in range(9)
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