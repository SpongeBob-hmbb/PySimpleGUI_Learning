# 导入库
import PySimpleGUI as sg


list = ['python','java','c++','php','html']
# 定义布局，确定行数
layout = [
    [sg.LB(list,
    default_values = None,#默认选中的值或者列表
    key = None,# 元素唯一标识符
    select_mode = None,#选择模式
    #single 单选，更换时点击选择
    #multiple可以多选，逐一点击选择
    # browse 单选，鼠标按住时也可更换选择
    # extended 可以多选，鼠标按住是可以扩展选择
    enable_events = False,# 元素事件属性
    #为True 元素列表被选中时会发生事件
    bind_return_key = False,# 绑定回车健
    #为True,回车键按下时相当于此元素被点击
    size = (10,6),# 字符宽度 行高
    disabled = False,# 元素是否被禁用
    auto_size_text = None,# 为True自动调整大小
    font = None,# 设置字体名称 大小
    no_scrollbar = False, #为True 则没有滚动条
    background_color = None,# 背景颜色
    text_color = None, # 字体颜色
    pad = None, # 元素间隔设定
    tooltip = None,# 悬浮文本
    right_click_menu = None, # 右击调出菜单
    visible = True,# 元素可见状态

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