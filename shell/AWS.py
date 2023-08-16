from util.location.AWS import okExposure
from util.misc import advancedClick


def clickOK():
    x, y = okExposure()
    advancedClick(x, y)
