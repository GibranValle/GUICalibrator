import time
import customtkinter as ck

from util.location.location import isExposing
from util.location.location_AWS import stdbyIcon, blockedIcon

stopFlag = False


def genericCounter(label, init, final, minTime, breakCondition, text):
    global stopFlag
    count = range(init, final + 1)
    if final < init:
        count = range(init, final - 1, -1)
    global stopFlag
    secs = 0
    for c in count:
        secs += 1
        message = createMessage(text, c)
        editOutput(message, label)
        time.sleep(1)
        if breakCondition() and secs >= minTime:
            return secs
        elif stopFlag:
            return -1
    return secs


def countdown(label, final, text='', init=0):
    minTime = 0
    breakCondition = Pass
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


def waitTillEnd(init, final, label: ck.CTkLabel):
    minTime = 4
    breakCondition = isBlocked
    text = 'Waiting for end'
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


def waitTillReady(init, final, label: ck.CTkLabel):
    minTime = 5
    breakCondition = isStdBy
    text = 'Waiting for next'
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


def waitTillStartYellow(final, label: ck.CTkLabel, init=0):
    minTime = 3
    breakCondition = isExposureNotDone
    text = 'Wait for start'
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


def waitTillEndYellow(final, init, label: ck.CTkLabel):
    minTime = 20
    breakCondition = isExposureDone
    text = 'Wait for end'
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


# --------------------------- AUXILIARY -----------------------------------------------------------

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

def getStopFlag():
    global stopFlag
    return stopFlag


def setStopFlag():
    global stopFlag
    stopFlag = True


def resetStopFlag():
    global stopFlag
    stopFlag = False


def editOutput(text, label: ck.CTkLabel):
    label.configure(text=text)


def editButton(text, button: ck.CTkButton):
    button.configure(text=text, fg_color='#003366', hover_color='#002255')


def createMessage(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'{msg}: {secs}s' if minutes <= 0 else f'{msg}: {minutes}m {secs}s'
    return text


def Pass():
    return False
