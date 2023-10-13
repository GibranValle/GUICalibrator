import pyautogui
import os
from util.CustomExceptions import IconNotFoundError

path = os.getcwd()


def genericCoordinates(
    name: str, confidence: float = 0.75
) -> tuple[int, int, int, int]:
    try:
        x, y, w, h = pyautogui.locateOnScreen(f"{path}/img/{name}.png", confidence=confidence)  # type: ignore
    except TypeError:
        raise IconNotFoundError(f"{name} NOT FOUND")
    else:
        return x, y, w, h  # type: ignore


def genericCoordinatesCenter(name: str, confidence: float = 0.75) -> tuple[int, int]:
    try:
        x, y = pyautogui.locateCenterOnScreen(f"{path}/img/{name}.png", confidence=confidence)  # type: ignore
    except TypeError:
        raise IconNotFoundError(f"{name} NOT FOUND")
    else:
        return x, y  # type: ignore
