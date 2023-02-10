# 导入库
import PySimpleGUI as sg

list = ['非常满意','满意','一般','不满意']

# 定义布局，确定行数
layout = [
    [sg.T('请对课程进行评价：')],
    [sg.R(i,group_id = 1,key = i)for i in list],
    [sg.B('确认提交')]
    ]

# 创建窗口
window = sg.Window('Python GUI',layout)

# 事件循环
while True:
    event,values = window.read()

    if event == None:
        break
    if event == '确认提交':
        #window['满意'].ResetGroup() # 单选框清空
        # window['满意'].update(value = True) # 点击确定后选择满意
        for k,v in values.items():
            if v == True:
                print(k) # 获取选择的结果
# 关闭窗口
window.close()