# 导入库
import PySimpleGUI as sg

# 主题
# sg.theme('GrayGrayGray')

lista = ['苹果','香蕉','雪梨','西瓜']
listb = ['萝卜','白菜','包菜','青菜']
tab1_layout = [[sg.LB(lista,size=(50,5))]]
tab2_layout = [[sg.LB(listb,size=(50,5))]]
# 定义布局，确定行数
layout =[
    [sg.TabGroup([[sg.Tab('水果',tab1_layout,element_justification="center",background_color='black'),sg.Tab('蔬菜',tab2_layout)]],
    background_color='red',
    tab_background_color='green',
    selected_background_color='blue',
    selected_title_color='yellow',
    border_width='10')
    ]
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
