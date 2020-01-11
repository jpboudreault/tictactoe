from .center import *
from .first import *
from .random import *
from .xavier import *


def get_cpu(code):
    if code == 'first':
        return First()
    elif code == 'rand':
        return Random()
    elif code == 'xav':
        return Xavier()
    elif code == 'center':
        return Center()
    else:
        raise NotImplementedError("The cpu with the code %s could not be found" % code)
