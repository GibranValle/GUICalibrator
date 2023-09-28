from time import sleep
from customtkinter import CTk as ck
from classes.generic import createMessage
from util.location.AWS import stdbyIcon, blockedIcon, okExposure, pasarIcon, saltarIcon, exposureIcon, \
    exposureIconLarge, calibracionIcon, okExposure_green
from shell.AWS import clickOK


class DelayManager:
    def __init__(self, gui_object: ck):
        self.status = 'stop'
        self.gui = gui_object

    def _generic_counter(self, init: int, final: int, minTime: int, breakCondition, text: str,
                         wait_calib_pass: bool = True):

        if self.status == 'stop':
            return -1

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
            if isCalibPass() and wait_calib_pass:
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

    def wait_for_block_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isBlocked
        text = 'Waiting for blocked'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def wait_for_exposure_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isExposing
        text = 'Waiting for exposure'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def wait_for_stdby_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isStdBy
        text = 'Waiting for standby'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def wait_for_long_end(self, final: int, init: int):
        minTime = 20
        breakCondition = isExposureDone
        text = 'Wait for end'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def wait_for_calib_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isCalibratingFPD
        text = 'Waiting for Calib start'
        secs = self._generic_counter(init, final, minTime, breakCondition, text, wait_calib_pass=False)
        return secs

    def wait_for_calib_pass(self, init: int, final: int):
        minTime = 0
        breakCondition = isCalibPass
        text = 'Waiting for Pass'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        return secs

    def wait_for_ok_button(self, final: int, init: int):
        minTime = 1
        breakCondition = isWaitingOk
        text = 'Wait for ok button'
        secs = self._generic_counter(init, final, minTime, breakCondition, text, wait_calib_pass=False)
        return secs


# --------------------------- AUXILIARY -----------------------------------------------------------

def isCalibratingFPD():
    x, y = calibracionIcon()
    if x > 0 and y > 0:
        return True
    return False


def isWaitingOk():
    x, y = okExposure()
    if x > 0 and y > 0:
        return True
    x, y = okExposure_green()
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
    x, y = exposureIconLarge()
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
