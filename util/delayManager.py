import time
import threading as th
import sys
from util.location import blockedIcon, stdbyIcon, isExposing
from multiprocessing.pool import ThreadPool


def editOutput(line2, label_output2=None):
    if len(line2) > 0:
        label_output2.configure(text=line2)


def createText(msg, count):
    minutes = count // 60
    secs = count % 60
    text = f'{msg}: {secs}s' if minutes <= 0 else f'{msg}: {minutes}m {secs}s'
    return text


def waitTillEnd(init, final, label_output2):
    """
    Delay of n secs until blocked icon is displayed on screen.
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 3
    secsPassed = 0
    for c in range(init, final + 1):
        time.sleep(1)
        secsPassed += 1
        text = createText('Exposure end', secsPassed)
        editOutput(text, label_output2)
        if (isBlocked() and c >= minTime) or c == final:
            break
    return secsPassed


def waitTillReady(init, final, label_output2):
    """
    Delay of n secs until standby icon is displayed on screen.
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 10
    secsPassed = 0
    for c in range(init, final + 1):
        time.sleep(1)
        secsPassed += 1
        text = createText('Next exposure', secsPassed)
        editOutput(text, label_output2)
        if (isStdBy() and c >= minTime) or c == final:
            break
    return secsPassed


def waitTillEndYellow(final, init, label_output2):
    """
    Delay of n secs until blocked icon is displayed on screen, reverse count
    :param init: initial count in secs
    :param final: final count in secs
    :return: breaks if icon is found
    """
    minTime = 60*10
    secsPassed = 0
    for c in range(init, final - 1):
        time.sleep(1)
        secsPassed += 1
        text = createText('Exposure end', secsPassed)
        editOutput(text, label_output2)
        if (isExposureDone() and c >= minTime) or c == final:
            break
    return secsPassed


def keyboardDelay(init, final, message, label_output2):
    passed = 0
    count = range(init, final + 1)
    if init > final:
        count = range(init, final, -1)
    for _ in count:
        passed += 1
        text = createText(f'{message} ', passed)
        editOutput(text, label_output2)
        clearLine()
        time.sleep(1)
    clearLine()
    text = createText('Time waited', passed)
    editOutput(text, label_output2)
    return passed


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
