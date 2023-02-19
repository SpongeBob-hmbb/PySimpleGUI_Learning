# 导入库
import PySimpleGUI as sg

# 主题
sg.theme('GrayGrayGray')


list=['资料1','资料2','资料3','资料4']
# 定义布局，确定行数
layouta =[
    [sg.T('账号'),sg.In()],
    [sg.T('密码'),sg.In()],
    [sg.B('确定'),sg.B('取消')]
]

layoutb = [
    [sg.LB(list,size=(30,5))]
]

layout = [
    [sg.Frame(title='登录框',layout = layouta,key='-a-'),
    sg.Frame(title='资料列表',layout=layoutb,visible=False,key='-b-')]
]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break

    if event == '确定':
        window['-a-'].update(visible=False)
        window['-b-'].update(visible=True)
# 关闭窗口
window.close()
