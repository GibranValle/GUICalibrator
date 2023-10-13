from util.misc import printError


class IconNotFoundError(Exception):
    "Exception raised when icon is not found in screen"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)


class AbortionRequestError(Exception):
    "Exception raised when user push stop"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)


class ExposureTooLongError(Exception):
    "Exception raised when exposure takes longer than permitted"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)


class ExposureTooShortError(Exception):
    "Exception raised when exposure takes longer than permitted"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)


class AbnormalBehaviorError(Exception):
    "Exception raised when generic malfunction of app occurs"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)


class AlreadySelectedError(Exception):
    "Exception raised when button is already selected"

    def __init__(self, message: str = ""):
        self.message = message
        printError(message)
        super().__init__(self.message)
