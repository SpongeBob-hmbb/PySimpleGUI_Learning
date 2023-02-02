# 导入库
import PySimpleGUI as sg

User1 = {'用户名':'1','密码':'135'}
User2 = {'用户名':'2','密码':'246'}
UserList = [User1,User2]

# 定义布局，确定行数
layout = [
    [sg.T('用户名',size=(8)),sg.In('请输入用户名',key='-user-')],
    [sg.T('密码',size=(8)),sg.In('',tooltip='密码为三位数字',password_char='*',key='-pwd-')],
    [sg.B('确定'),sg.B('取消')]
]

# 创建窗口
window = sg.Window('Python GUI',layout,keep_on_top=None)
msg = None

# 事件循环
while True:
    event,values = window.read()
    if event == None:
        break
    if event == '确定':
        for user in UserList:
            if values['-user-'] == user['用户名'] and values['-pwd-'] == user['密码']:
                msg='输入正确！'
                break
            else:
                msg='输入错误！'
        sg.Popup(msg)
            
# 关闭窗口
window.close()