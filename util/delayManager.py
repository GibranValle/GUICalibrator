from time import sleep
from customtkinter import CTk as ck
from util.location.AWS import stdbyIcon, blockedIcon, isExposing, okExposure, pasarIcon, saltarIcon
from classes.generic import Generic


class DelayManager:
    def __init__(self, gui_object: ck):
        self.stopFlag = False
        self.pauseFlag = False
        self.gui = gui_object

    def _generic_counter(self, init: int, final: int, minTime: int, breakCondition, text: str):
        print('generic counter')
        count = range(init, final + 1)
        if final < init:
            count = range(init, final - 1, -1)
        secs = 0
        for c in count:
            if self.stopFlag:
                return -1
            secs += 1
            message = createMessage(text, c)
            self.gui.generic.edit_output('', message)
            sleep(1)
            if breakCondition() and secs >= minTime:
                return secs
        return secs

    def resetFlags(self):
        self.stopFlag = False
        self.pauseFlag = False

    def countdown(self, final: int, text: str = '', init: int = 0):
        minTime = 0
        breakCondition = Pass
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillEnd(self, init: int, final: int):
        minTime = 3
        breakCondition = isBlocked
        text = 'Waiting for end'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillReady(self, init: int, final: int):
        print('waiting till ready signal')
        minTime = 1
        breakCondition = isStdBy
        text = 'Waiting for ready'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillStartYellow(self, final: int, init: int = 0):
        minTime = 5
        breakCondition = isExposureNotDone
        text = 'Wait for start'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillEndYellow(self, final: int, init: int):
        minTime = 20
        breakCondition = isExposureDone
        text = 'Wait for end'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillOk(self, final: int, init: int):
        minTime = 1
        breakCondition = isWaitingOk
        text = 'Wait for request'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs


# --------------------------- AUXILIARY -----------------------------------------------------------

def isWaitingOk():
    x, y = okExposure()
    if x > 0 and y > 0:
        return True
    return False


def isStdBy():
    x, y = stdbyIcon()
    if x > 0 and y > 0:
        return True
    return False


def isBlocked():
    x, y = blockedIcon()
    if x > 0 and y > 0:
        return True
    return False


def isExposureDone():
    x, y = isExposing()
    if x > 0 and y > 0:
        return False
    return True


def isExposureNotDone():
    x, y = isExposing()
    if x > 0 and y > 0:
        return True
    return False


def isCalibPass():
    x, y = pasarIcon()
    if x > 0 and y > 0:
        return True
    x, y = saltarIcon()
    if x > 0 and y > 0:
        return True
    return False


def createMessage(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'{msg}: {secs}s' if minutes <= 0 else f'{msg}: {minutes}m {secs}s'
    return text
