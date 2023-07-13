import subprocess
import time

import win32gui as w
import win32con as c
from pyautogui import moveTo, click

from util.location.location_MUTL import MU_page_0, right, calibration_MU, generator_MU


def openRU():
    if process_exists('RuPcTool.exe'):
        return openWindow('RU PC-TOOL')
    openApp('RUPCTOOL')


def closeRU():
    name = 'RuPcTool.exe'
    closeApp(name)


def openMUTLMU():
    if process_exists('MUTL.exe'):
        return openWindow('MU0')
    openApp('MU')


def closeMUTL():
    name = 'MUTL.exe'
    closeApp(name)


def openCalibrationMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = calibration_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return


def openGeneratorMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = generator_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return


def openWindow(name):
    def handler(hwnd, active):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            if active in wname:
                w.SetForegroundWindow(hwnd)
                w.ShowWindow(hwnd, c.SW_NORMAL)

    w.EnumWindows(handler, name)
    time.sleep(0.5)


def scanWindows():
    file = open("windowNames.txt", "w")

    def handler(hwnd, param):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            size = len(wname)
            if size > 0:
                file.writelines(wname + '\n')

    w.EnumWindows(handler, None)
    file.close()


def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call)
    # print(output)
    output = output.decode('latin-1')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # print(last_line)
    # print(last_line)
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def openApp(appName):
    try:
        if appName == 'RUPCTOOL':
            route = 'C:\Program Files\Fujifilm\FCR\TOOL\RuPcTool\\'
            exe = 'RuPcTool'
            args = ''
            subprocess.Popen(route + exe + args)

        elif appName == 'MU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.100 /RUNAME:MU0 /TYPE:FDR-2500A'
            subprocess.Popen(route + exe + args)

        elif appName == 'MCU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.101 /RUNAME:MCU0 /TYPE:FDR-3000DRL /FCR:C:\Program Files\FujiFilm\FCR\\'
            subprocess.Popen(route + exe + args)
        time.sleep(0.5)
    except FileNotFoundError:
        print('File not found')


def closeApp(appName):
    if process_exists(appName):
        subprocess.call(["taskkill", "/F", "/IM", appName],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.5)
