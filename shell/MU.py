

def openCalibrationMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = calibration_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return

def openGeneratorMUMenu():
    openMUTLMU()
    # is MCU FIRST PAGE?
    x, y = MU_page_0()
    if x > 0 and y > 0:
        # NO FIRST PAGE, CHANGE TO NEXT
        x, y = right()
        if x > 0 and y > 0:
            moveTo(x, y, duration=0.5)
            click(x, y)

    x, y = generator_MU()
    if x > 0 and y > 0:
        moveTo(x, y, duration=0.5)
        click(x, y)
        return
