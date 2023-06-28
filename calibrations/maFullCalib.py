import time

def mAFullCalibration():
    print(f"ma full calibration selected")
    print(f"Estimated waiting time: 20 mins")
    print("----------------------------------------------------")
    print(f"<-- Requesting exposure 1 of 1 -->")
    if not communicate("T"):     # VERIFY CONNECTION BEFORE COUNTDOWN
        return
    print("\n>-- Exposure request accepted --< ")
    editOutput('>-- Exposure request accepted --<', '')
    keyboardDelay(10, 0, ' Starting exposure in: ')
    if not communicate("L"):     # REQUEST FOR LONG EXPOSURE
        return
    time = waitTillEndYellow(5*60, 0)
    print(" <-- Requesting end of exposure -->")
    if not communicate("X"):
        return
    print(" >-- Exposure done --< ")
    keyboardDelay(15*60, 0, ' Calculating: ')
