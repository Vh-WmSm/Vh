import public_tools

gui = public_tools.PySimpleGUI_Tool(['被减:', '减:'], '时间相减小工具(时 分)', '开始相减', title_size=4, in_size=30, start_button_size=30)
while True:
    beijian, jian = gui.gui_windows()
    beijian_list = list(map(int, beijian.split()))
    jian_list = list(map(int, jian.split()))
    gui.popup_scrolled(str(abs((beijian_list[0] - jian_list[0]) * 60 + (beijian_list[1] - jian_list[1]))))
