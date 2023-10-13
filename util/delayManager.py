from typing import Any

from time import sleep
from classes.generic import createMessage
from util.location.AWS import (
    stdbyIcon,
    blockedIcon,
    okExposure,
    pass_icon,
    saltar_icon,
    exposureIcon,
    exposureIconLarge,
    fpd_calibrating,
    okExposure_green,
)
from shell.AWS import clickOK
from util.CustomExceptions import (
    IconNotFoundError,
    AbnormalBehaviorError,
    AbortionRequestError,
)
from classes.constants import AWS_STATUS, aws_status


class DelayManager:
    def __init__(self, gui_object: Any):
        self.status = "stop"
        self.gui = gui_object

    def _generic_counter(
        self,
        init: int,
        final: int,
        minTime: int,
        breakCondition: Any,  # type: ignore
        text: str,
    ) -> int:
        count = range(init, final + 1) if final > init else range(init, final - 1, -1)
        secs = 0
        for c in count:
            if self.status == "stop":
                raise AbortionRequestError("STOP BUTTON PUSHED")
            while self.status == "pause":
                sleep(1)
            if check_status(breakCondition) and secs >= minTime:
                return secs
            if self.gui.is_auto_ok:
                clickOK()
            secs += 1
            self.gui.generic.edit_subtitle(createMessage(text, c))
            sleep(1)
        return secs

    def startStatus(self):
        self.status = "start"

    def pauseStatus(self):
        self.status = "pause"

    def stopStatus(self):
        self.status = "stop"

    def countdown(
        self, init: int = 10, text: str = "Requesting exposure in", final: int = 0
    ) -> int:
        minTime = 0
        breakCondition = None
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > init + 1:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_block_signal(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isBlocked"
        text = "Waiting: blocked signal"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_exposure_signal(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isExposing"
        text = "Waiting: exp start"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_no_exposure_signal(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isExposureDone"
        text = "Waiting: exp end"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_stdby_signal(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isStdBy"
        text = "Waiting: stdby signal"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_long_end(self, final: int, init: int):
        minTime = 20
        breakCondition: aws_status = "isExposureDone"
        text = "Waiting: long exp end"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_calib_signal(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isCalibratingFPD"
        text = "Waiting: calib start"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_calib_pass(self, init: int, final: int):
        minTime = 1
        breakCondition: aws_status = "isCalibPass"
        text = "Waiting: calib pass"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs

    def wait_for_ok_button(self, final: int, init: int):
        minTime = 1
        breakCondition: aws_status = "isWaitingOk"
        text = "Waiting: ok button"
        secs = self._generic_counter(init, final, minTime, breakCondition, text)
        if secs > final:
            raise AbnormalBehaviorError("Secs cannot be greater than expected")
        return secs


# --------------------------- AUXILIARY -----------------------------------------------------------


def check_status(status: aws_status) -> bool:
    if status not in AWS_STATUS:
        return False
    try:
        if status == "isCalibratingFPD":
            fpd_calibrating()

        elif status == "isWaitingOk":
            try:
                okExposure()
            except IconNotFoundError:
                pass
            okExposure_green()

        elif status == "isStdBy":
            stdbyIcon()

        elif status == "isBlocked":
            blockedIcon()

        elif status == "isExposing":
            try:
                exposureIcon()
            except IconNotFoundError:
                pass
                exposureIconLarge()

        elif status == "isExposureDone":
            try:
                exposureIcon()
                return False
            except IconNotFoundError:
                pass
                exposureIconLarge()
                return False

        elif status == "isCalibPass":
            try:
                pass_icon()
            except IconNotFoundError:
                pass
                saltar_icon()

        return True
    except IconNotFoundError:
        if status == "isExposureDone":
            return True
        return False
