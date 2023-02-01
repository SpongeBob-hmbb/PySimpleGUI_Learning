# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [sg.T('帐号: '),sg.In(
    '请输入您的帐号', # 默认值设定，可以为空字符串。
    key = '-INPUT-', # 元素的唯一标识符 规范key= '-INPUT-'
    size = (None,None), # 宽,行高
    disabled = None, # bool: 元素禁用，如果为True 则禁用，无法输入任何值。
    password_char = '', # 密码字符, 一般设置为*
    justification = 'l', # 对齐方式'r','L', 'c'
    background_color=None,#输入框的颜色
    text_color=None,#输入框的文本颜色
    font = None, # 字体
    tooltip = None, # str 悬浮文本
    border_width = None, # 输入框边界线宽度设定
    enable_events = False, # bool 输入框事件属性
                            # 为True时，输入会发生一个事件
    do_not_clear = True, # bool输入内容不被清除
                            # 为False，一发生事件，该输入框内的值会清空
    focus = False, # bool 设定焦点，为True时，则光标显示在此输入框
    pad = None, # 元素间隔
    disabled_readonly_background_color = None, # str元素禁用时背景颜色设定
    disabled_readonly_text_color = None, # str元素禁用时文字颜色设定
    right_click_menu = None, # 右击按钮菜单List[List[Union[List[str],str]]]
                            # 设定后，右击此元素会调出菜单
    visible = True # 元素的可见状态，为False时不可见
        )],
    [sg.T('密码'),sg.In('')],
    [sg.B('确定'),sg.B('取消')]
]


# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()
    print(event)
    if event == None:
        break

# 关闭窗口
window.close()