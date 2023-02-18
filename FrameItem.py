# 导入库
import PySimpleGUI as sg

# 主题
sg.theme('GrayGrayGray')

# 定义布局，确定行数
layouta =[
    [sg.T('账号'),sg.In()],
    [sg.T('密码'),sg.In()]
]

layout = [
    [sg.Frame(title='登录框',layout = layouta,
    title_color='red',
    # 标题文本颜色设定

    background_color='yellow',
    # 框架背景颜色设定

    title_location='wn',
    # 标题所在位置
    # 有效值有12种
    # s n w e 排列组合

    relief="groove",
    # 浮雕设计

    size = (None,None),

    font = None,
    # 字体名称，大小

    pad=None,

    border_width=None,
    # 框架元素的线条宽度
    
    key = None,

    tooltip=None,

    right_click_menu=None,
    visible=True,
    element_justification="left",
    vertical_alignment=None,
    # 垂直对齐方式
    )]
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
