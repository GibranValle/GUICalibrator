from generic import changeWindow, openApp, closeApp

def openRU():
    if process_exists('RuPcTool.exe'):
        return changeWindow('RU PC-TOOL')
    openApp('RUPCTOOL')


def closeRU():
    name = 'RuPcTool.exe'
    closeApp(name)


def closeMUTL():
    name = 'MUTL.exe'
    closeApp(name)