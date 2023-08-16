from time import sleep
from customtkinter import CTk as ck

from classes.generic import createMessage
from util.location.AWS import stdbyIcon, blockedIcon, isExposing, okExposure, pasarIcon, saltarIcon, exposureIcon
from shell.AWS import clickOK

class DelayManager:
    def __init__(self, gui_object: ck):
        self.status = 'stop'
        self.gui = gui_object

    def _generic_counter(self, init: int, final: int, minTime: int, breakCondition, text: str):
        count = range(init, final + 1)
        if final < init:
            count = range(init, final - 1, -1)
        secs = 0
        for c in count:
            if self.status == 'stop':
                return -1
            elif self.status == 'pause':
                while self.status == 'pause':
                    sleep(1)
                    print('pause on')
            if isCalibPass():
                return secs
            if breakCondition() and secs >= minTime:
                return secs
            if self.gui.is_auto_ok:
                clickOK()

            secs += 1
            message = createMessage(text, c)
            self.gui.generic.edit_output('', message)
            sleep(1)
        return secs

    def startStatus(self):
        self.status = 'start'

    def pauseStatus(self):
        self.status = 'pause'

    def stopStatus(self):
        self.status = 'stop'

    def countdown(self, final: int, text: str = '', init: int = 0):
        minTime = 0
        breakCondition = isCalibPass
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillEnd(self, init: int, final: int):
        minTime = 0
        breakCondition = isBlocked
        text = 'Waiting for blocked'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillExposing(self, init: int, final: int):
        minTime = 0
        breakCondition = isExposing
        text = 'Waiting for exposure'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillReady(self, init: int, final: int):
        minTime = 0
        breakCondition = isStdBy
        text = 'Waiting for standby'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def waitTillStartYellow(self, final: int, init: int = 0):
        minTime = 5
        breakCondition = isExposureNotDone
        text = 'Wait for exposure'
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
        text = 'Wait for ok button'
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


def isExposing():
    x, y = exposureIcon()
    if x > 0 and y > 0:
        return True
    return False


def isExposureDone():
    return not isExposing()


def isExposureNotDone():
    return isExposing()


def isCalibPass():
    x, y = pasarIcon()
    if x > 0 and y > 0:
        return True
    x, y = saltarIcon()
    if x > 0 and y > 0:
        return True
    return False
