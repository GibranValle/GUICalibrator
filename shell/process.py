import subprocess
import time

import win32gui as w
import win32con as c
import util.location as loc
import pyautogui as pg


def openChrome():
    if process_exists('chrome.exe'):
        return openWindow('Chrome')
    openApp('Chrome')


def closeChrome():
    name = 'chrome.exe'
    closeApp(name)


def openRU():
    if process_exists('RuPcTool.exe'):
        return openWindow('RU PC-TOOL')
    openApp('RUPCTOOL')


def closeRU():
    name = 'RuPcTool.exe'
    closeApp(name)


def openMUTLMU():
    if process_exists('MUTL.exe'):
        return openWindow('PC-MUTL MU')
    openApp('MU')


def openMUTLMCU():
    if process_exists('MUTL.exe'):
        return openWindow('PC-MUTL MCU')
    openApp('MCU')


def closeMUTL():
    name = 'MUTL.exe'
    closeApp(name)


def openCalibrationMenuMouse():
    openMUTLMCU()

    x, y = loc.calibration()
    if x > 0 and y > 0:
        return print('BUTTON FOUND')

    x, y = loc.right()
    if x > 0 and y > 0:
        return print('RIGHT FOUND')


def openCalibrationOptionalMenuMouse():
    openMUTLMCU()

    x, y = loc.calibrationOptional()
    if x > 0 and y > 0:
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)
        return

    x, y = loc.right()
    if x > 0 and y > 0:
        pg.moveTo(x, y, duration=0.5)
        pg.click(x, y)
        x, y = loc.calibrationOptional()
        if x > 0 and y > 0:
            pg.moveTo(x, y, duration=0.5)
            pg.click(x, y)
            return


def startOffsetCalib():
    openCalibrationMenuMouse()
    x, y = loc.offset()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startDefectCalib():
    openCalibrationMenuMouse()
    x, y = loc.defect()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startDefectSolidCalib():
    openCalibrationMenuMouse()
    x, y = loc.defectSolid()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startPixelDefectCalib():
    openCalibrationMenuMouse()
    x, y = loc.pixelDefect()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startShadingCalib():
    openCalibrationMenuMouse()
    x, y = loc.shading()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityCalib():
    openCalibrationMenuMouse()
    x, y = loc.shading()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startDefectSolidStereoCalib():
    openCalibrationMenuMouse()
    x, y = loc.defectSolidStereo()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startDefectSolidBpyCalib():
    openCalibrationMenuMouse()
    x, y = loc.defectSolidBpy()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startDefectSolidTomo():
    openCalibrationMenuMouse()
    x, y = loc.defectSolidTomo()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityStereoCalib():
    openCalibrationMenuMouse()
    x, y = loc.offset()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityBpyCalib():
    openCalibrationMenuMouse()
    x, y = loc.uniformityBpy()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityTomoCalib():
    openCalibrationMenuMouse()
    x, y = loc.uniformityTomo()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)


def startUniformityESCalib():
    openCalibrationMenuMouse()
    x, y = loc.uniformityES()
    if x <= 0 and y <= 0:
        return
    pg.moveTo(x, y, duration=0.5)
    pg.click(x, y)
# __________________________________________________________________


def openWindow(name):
    def handler(hwnd, active):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            if active in wname:
                w.SetForegroundWindow(hwnd)
                w.ShowWindow(hwnd, c.SW_NORMAL)
    w.EnumWindows(handler, name)


def scanWindows():
    file = open("windowNames.txt", "w")
    def handler(hwnd, param):
        if w.IsWindowVisible(hwnd):
            wname = w.GetWindowText(hwnd)
            size = len(wname)
            if size > 0:
                file.writelines(wname+'\n')
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
    #print(last_line)
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

    except FileNotFoundError:
        print('File not found')


def closeApp(appName):
    if process_exists(appName):
        subprocess.call(["taskkill", "/F", "/IM", appName],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def getMacList():
    call = 'chcp 65001 | getmac /fo csv /v /nh'
    output = subprocess.check_output(call, shell=True)
    output = output.decode('utf-8').split('\r\n')
    ethernet = []
    for index, line in enumerate(output):
        items = line.split(',')
        if "Ethernet" in items[0]:
            ethernet.append(items[2].replace('"', '').replace('-', ':'))
    # print(ethernet)
    return '\n'.join(ethernet)


def getMac(ip):
    try:
        call = 'arp', '-a', ip
        output = subprocess.check_output(call)
        output = output.decode('latin-1').strip().split('\r\n')
        lines = output[3:]
        for item in lines:
            line = []
            print(item)
            subarray = item.strip().split(' ')
            for subitem in subarray:
                line.append(subitem) if len(subitem) > 0 else 0
            if line[0] == ip:
                return line[1].replace('-',':')
        return 'IP address not found!'
    except IndexError:
        print(output)


def getMac(ip):
    call = 'arp', '-a', ip
    output = subprocess.check_output(call)
    output = output.decode('latin-1').strip().split('\r\n')
    try:
        lastLine = output[2:][0].split(' ')
        for item in lastLine:
            if len(item) > 0 and '-' in item:
                return item.upper().replace('-', ':')
        return 'IP not found'
    except IndexError:
        return 'IP not found'


def getMCUMac():
    return getMac('192.168.0.101')


def saveMACs():
    other = getMacList()
    mcu = getMCUMac()
    f = open('macList.txt', 'w')
    f.writelines('LOCAL:\n')
    f.writelines(other+'\n')
    f.writelines('MCU0:\n')
    f.writelines(mcu)
    f.close()
    temp = 'LOCAL', other, 'MCUO:', mcu
    return '\n'.join(temp)
