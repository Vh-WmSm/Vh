import PySimpleGUI as sg
import sys

def float_(Pt, DSR, Pr, Pp, namuda, Me, am,  a, Lf, As, Ac, fb):
    return [float(Pt), float(DSR), float(Pr), float(Pp), float(namuda), float(Me), float(am), float(a), float(Lf), float(As), float(Ac), float(fb)]
Pt_DSR_Pr_Pp = '';judge = '';namuda = '';Me = '';am = '';a = '';Lf = '';As = '';Ac = '';fb = '';jud = ''
while True:
    layout = [
        [sg.Text('{:<21}'.format('Pt_DSR_Pr_Pp:')), sg.In(Pt_DSR_Pr_Pp)],
        [sg.Text('{:<18}'.format('G652/G654？(1或2):')), sg.In(judge)],
        [sg.Text('{:<27}'.format('namuda:')), sg.In(namuda)],
        [sg.Text('{:<18}'.format('设备富余度Me:')), sg.In(Me)],
        [sg.Text('{:<18}'.format('光缆富余度am:')), sg.Input(am)],
        [sg.Text('{:<22}'.format('啁啾系数a:')), sg.In(a)],
        [sg.Text('{:<19}'.format('单盘光缆盘长Lf:')), sg.In(Lf)],
        [sg.Text('{:<12}'.format('单个光纤接头损耗As:')), sg.In(As)],
        [sg.Text('{:<14}'.format('光纤连接器损耗Ac:')), sg.In(Ac)],
        [sg.Text('{:<16}'.format('标称比特率fb(GHz):')), sg.In(fb)],
        [sg.Text('{:<25}'.format('ITU-T？Y/N:')), sg.In(jud)],
        [sg.Button('开始设计')]
    ]
    windows = sg.Window('光纤设计计算器', layout, keep_on_top=True)  # 显示窗口
    while True:  # 设置窗口循环
        event, values = windows.read()  # 设置变量作为窗口显示内容
        if event == None:  # 设置关闭窗口事件
            sys.exit()
        if event == '开始设计':  # 设置点击“开始设计”按钮事件
            # 设置返回内容
            Pt_DSR_Pr_Pp = values[0]
            judge = values[1]
            namuda = values[2]
            Me = values[3]
            am = values[4]
            a = values[5]
            Lf = values[6]
            As = values[7]
            Ac = values[8]
            fb = values[9]
            jud = values[10]
        Pt, DSR, Pr, Pp = Pt_DSR_Pr_Pp.split(' ')
        Pt, DSR, Pr, Pp, namuda, Me, am, a, Lf, As, Ac, fb = float_(Pt, DSR, Pr, Pp, namuda, Me, am, a, Lf, As, Ac, fb)
        a_s = As / Lf
        if judge == '1':
            if namuda == 1550:
                af = 0.25
                D = 20
            else:
                af = 0.4
                D = 3.5
        else:
            namuda = 1550
            af = 0.18
            D = 22
        if jud == 'Y' or jud == 'y':
            LD = DSR / D
        else:
            LD = 71400 / (a * D * namuda ** 2 * (fb / 1000) ** 2)
        LL = (Pt - Pr - 2 * Ac - Me - Pp) / (af + a_s + am)
        print('损耗受限距离：LL = {:.2f}\n色散受限距离：LD = {:.2f}'.format(LL, LD))
        break
    windows.close()
