from time import sleep
from classes.generic import createMessage
from util.location.AWS import stdbyIcon, blockedIcon, okExposure, pasarIcon, saltarIcon, exposureIcon, \
    exposureIconLarge, calibracionIcon, okExposure_green
from shell.AWS import clickOK
from util.misc import printSuccess


class DelayManager:
    def __init__(self, gui_object):
        self.status = 'stop'
        self.gui = gui_object

    def _generic_counter(self, init: int, final: int, minTime: int, breakCondition, text: str,
                         calib_pass_flag: bool = True):

        if self.status == 'stop':
            return -1

        count = range(init, final + 1)
        if final < init:
            count = range(init, final - 1, -1)
        secs = 0
        for c in count:
            if breakCondition:
                print(breakCondition())
            if self.status == 'stop':
                return -1
            if self.status == 'pause':
                while self.status == 'pause':
                    sleep(1)
            if isCalibPass() and calib_pass_flag:
                printSuccess(f'CALIB PASS SIGNAL FOUND!')
                return secs
            if breakCondition and breakCondition() and secs >= minTime:
                printSuccess(f'BREAK CONDITION')
                return secs
            if self.gui.is_auto_ok:
                clickOK()

            secs += 1
            self.gui.generic.edit_subtitle(createMessage(text, c))
            sleep(1)
        if secs < 0:
            raise ValueError('Secs must be greater than 0')
        print('EXIT GENERIC COUNTER')
        return secs

    def startStatus(self):
        self.status = 'start'

    def pauseStatus(self):
        self.status = 'pause'

    def stopStatus(self):
        self.status = 'stop'

    def countdown(self, init: int = 10, text: str = 'Requesting exposure in', final: int = 0):
        if init <= 0:
            return -1
        minTime = 0
        breakCondition = None
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        print(secs, init)
        if secs > init + 1:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_block_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isBlocked
        text = 'Waiting for blocked'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_exposure_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isExposing
        text = 'Waiting for exposure'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        print(secs)
        print('EXPOSURE FOUND')
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_no_exposure_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isExposureDone
        text = 'Waiting for exposure end'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_stdby_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isStdBy
        text = 'Waiting for standby'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_long_end(self, final: int, init: int):
        minTime = 20
        breakCondition = isExposureDone
        text = 'Wait for end'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_calib_signal(self, init: int, final: int):
        minTime = 0
        breakCondition = isCalibratingFPD
        text = 'Waiting for Calib start'
        secs = self._generic_counter(init, final, minTime, breakCondition, text, calib_pass_flag=False)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_calib_pass(self, init: int, final: int):
        minTime = 0
        breakCondition = isCalibPass
        text = 'Waiting for Pass'
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
        return secs

    def wait_for_ok_button(self, final: int, init: int):
        minTime = 1
        breakCondition = isWaitingOk
        text = 'Wait for ok button'
        secs = self._generic_counter(init, final, minTime, breakCondition, text, calib_pass_flag=False)
        if secs > final:
            raise ValueError('Secs cannot be greater than expected')
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


def isCalibPass():
    x, y = pasarIcon()
    if x > 0 and y > 0:
        return True
    x, y = saltarIcon()
    if x > 0 and y > 0:
        return True
    return False
