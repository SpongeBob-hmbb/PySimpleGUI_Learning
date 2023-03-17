import PySimpleGUI as sg
month = ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
week = ['周日','周一','周二','周三','周四','周五','周六']
layout = [
    [sg.ColorChooserButton(button_text='颜色选择器'),sg.In()],
    [sg.CalendarButton(button_text='日历选择器',
                       close_when_date_chosen=True,
                       default_date_m_d_y=(1,2,2000),
                       format="%Y %m %d",
                       begin_at_sunday_plus=6, # 周六开始
                       month_names= month,
                       day_abbreviations=week,
                       title='日历',no_titlebar=False,
                       location=(100,100)
                       ),sg.In()]
]
window = sg.Window('演示窗口',layout)
while True:
    event,values = window.read()
    if event == None:
        break
window.close()