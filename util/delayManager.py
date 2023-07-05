import time
import threading as th
import sys
from util.location import blockedIcon, stdbyIcon, isExposing
from multiprocessing.pool import ThreadPool
import customtkinter as ck

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
            return -2
            break
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
    minTime = 15
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
    minTime = 60 * 4
    breakCondition = isExposureDone
    text = 'Wait for end'
    secs = genericCounter(label, init, final, minTime, breakCondition, text)
    return secs


# --------------------------- AUXILIARY -----------------------------------------------------------

def isStdBy():
    x, y = stdbyIcon()
    print(x, y)
    if x > 0 and y > 0:
        return True
    return False


def isBlocked():
    x, y = blockedIcon()
    print(x, y)
    if x > 0 and y > 0:
        return True
    return False


def isExposureDone():
    x, y = isExposing()
    print(x, y)
    if x > 0 and y > 0:
        return False
    return True


def isExposureNotDone():
    x, y = isExposing()
    print(x, y)
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


def editOutput(line2, label: ck.CTkLabel):
    label.configure(text=line2)


def createMessage(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'{msg}: {secs}s' if minutes <= 0 else f'{msg}: {minutes}m {secs}s'
    return text


def Pass():
    return False
