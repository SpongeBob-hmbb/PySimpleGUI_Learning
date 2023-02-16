# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layoutL = [
    [sg.T('标题')],
    [sg.In('请输入文章标题')],
    [sg.T('作者')],
    [sg.In('请输入姓名')]
]

layoutR=[
    [sg.ML('请输入正文内容',size=(30,20))],
    [sg.B('提交')]
]

layout =[
    [sg.Col(layoutL,
    background_color='black',
    # 背景颜色

    size=(None,None),
    # 宽度 高度

    pad = None,
    #与周围元素间的设定 左右上下

    scrollable=False,
    # 为True 滚动条添加到该列

    vertical_scroll_only=False,
    # 为True 不会显示水平滚动条

    right_click_menu=None,
    # 右键调出菜单

    key=None,

    visible=True,

    justification="left",
    # 为列本身设置对齐方式

    element_justification="center",
    # 列内所有元素的对齐方式
    # left right center

    vertical_alignment=None,
    #垂直对齐方式
    # top bottom center

    grab=None,
    #为True 可以拖拽移动窗口

    expand_x=None,
    # 为True 自动沿x方向扩展以填充可用空间

    expand_y=True,
    # 为True 自动沿y方向扩展以填充可用空间
    ),sg.Col(layoutR)]
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