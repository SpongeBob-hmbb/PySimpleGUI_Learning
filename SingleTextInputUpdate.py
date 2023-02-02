# 导入库
import PySimpleGUI as sg

# 定义布局，确定行数
layout = [
    [[sg.In(i,key=i)] for i in 'abcd'],
    [sg.B('确定'),sg.B('取消')]
]

# 创建窗口
window = sg.Window('Python GUI',layout,keep_on_top=True)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '确定':
        # window['d'].SetFocus() # 文本聚焦
        # window['d'].SetTooltip('这是悬浮文本') # 用于更新悬浮文本
        window['d'].update(
            value = '123', # str 更新输入框内的文本
            disabled = None, # bool 元素的禁用状态
                             # 为True 输入框变成只读状态，无法写入
            select = True, # bool 元素选中
                           # 为True 输入框内的文本全被选中
                           # 和focus 或 set_focus 一起试用
            visible = None, # bool 元素的可见状态
            text_color = None, # str 更新输入框内的文本颜色
            background_color =None, # str 更新输入框内的背景颜色
            move_cursor_to="end" # 光标移动到文本最后
                                 # 和value focus 一起试用
        )
# 关闭窗口
window.close()