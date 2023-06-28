import time
from util.macros import startMouseCalib
isFinished = False


def offsetCalib(timer):
    global isFinished
    print("Offset calibration selected")
    print("Estimated waiting time: 7 mins")
    print("Exposures required: 0")
    print("Starting offset calibration\n")
    startMouseCalib('offset')
    if timer:
        for i in range(1, 500):
            try:
                time.sleep(1)
                print(f"\rWaited time in secs {i}", end='')
            except KeyboardInterrupt:
                print('Delay aborted...')
    print("\n --Calibration complete-- \n")


def defectCalib(timer):
    global isFinished
    print("Defect calibration selected")
    print("Estimated waiting time: 7 mins")
    print("Exposures required: 0")
    print("Starting offset calibration\n")
    startMouseCalib('defect')
    if timer:
        for i in range(1, 500):
            try:
                time.sleep(1)
                print(f"\rWaited time in secs {i}", end='')
            except KeyboardInterrupt:
                print('Delay aborted...')
    print("\n --Calibration complete-- \n")


