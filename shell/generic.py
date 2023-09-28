import subprocess
from time import sleep
import win32gui as w
import win32con as c
import os

from util.misc import printError


def changeWindow(name):
    def handler(hwnd, active):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            if active in wname:
                w.SetForegroundWindow(hwnd)
                w.ShowWindow(hwnd, c.SW_NORMAL)

    print(f'Window {name} opened...')
    w.EnumWindows(handler, name)
    sleep(1)


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
            print(route, exe, args)
            subprocess.Popen(route + exe + args)

        elif appName == 'MCU':
            route = 'C:\Program Files\FujiFilm\FCR\TOOL\MUTL\\'
            exe = 'MUTL'
            args = ' /IP:192.168.0.101 /RUNAME:MCU0 /TYPE:FDR-3000DRL /FCR:C:\Program Files\FujiFilm\FCR\\'
            print(route, exe, args)
            subprocess.Popen(route + exe + args)
    except FileNotFoundError:
        printError('File not found')
    except OSError:
        printError('Program not installed')

    sleep(1)


def closeApp(appName):
    if process_exists(appName):
        subprocess.call(["taskkill", "/F", "/IM", appName],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        sleep(1)


def _scanWindows():
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
    # use build-in check_output right away
    output = subprocess.check_output(call)
    # print(output)
    output = output.decode('latin-1')
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # print(last_line)
    # print(last_line)
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())


def copyFile(origin, destiny):
    dir = os.getcwd()
    call = f'Xcopy {dir}\\{origin} {destiny}'
    output = subprocess.check_output(call, timeout=3)
    print(output)
