# 导入库
import PySimpleGUI as sg

# 主题
sg.theme('GrayGrayGray')

text = '''江南春
唐 杜牧
千里莺啼绿映红
水村山郭酒旗风
南朝四百八十寺
多少楼台烟雨中
'''

# 定义布局，确定行数
layout = [[sg.T(text, # sg.Text()缩写sg.T()
    key = '-Text-', # 元素唯一标识符，书写规范key = '-Name-' 用于元素定位
    size = (None,None), # 元素宽度 行高(int,int)
    font = None, # 设定字体的名称，大小 font='宋体' font=('宋体'，int) font=['宋体',int]
    auto_size_text = None, # 当设定值为True时，窗口自适应文本大小
    enable_events = None, # bool 事件属性 设定为True时，点击文本发生事件
    relief = None, # 浮雕设计 'raised' 'sunken' 'flat' 'ridge' 'solid' 'groove'
    border_width = None, # 设定relief时 用来设定边界宽度
    text_color = None, # 文本颜色
    background_color = None, # 文本背景颜色
    justification = None, # 对齐方式 'left' 'right' 'center'
    pad = None,  # 元素间隔设定 记住左右上下(int,int) ((int,int),(int,int))
                 #(int,(int,int)) ((int,int),int)
                 #(left/right,top/bottom) (left,right) (top,bottom)
    right_click_menu = None, # 右击调出菜单 List[List[Union[List[str],str]]] 
                             #设定后点击此元素可调出菜单
    grab = None, # 设定为True时 点击此元素可以移动脱拽窗口
    tooltip = None, # str:悬浮文本，当光标置于此元素上方时，会显示相应的文本
    visible = True # bool:元素可见状态
    )]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break

    if event == '-Text-':
        sg.Popup('运行了一个点击事件！')

# 关闭窗口
window.close()