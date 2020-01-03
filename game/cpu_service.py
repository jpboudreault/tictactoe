from ai.center import Center
from ai.first import First
from ai.random import Random
from ai.xavier import Xavier


class CpuService:

    def get_ai(self, code):
        if code == 'first':
            return First()
        elif code == 'rand':
            return Random()
        elif code == 'xav':
            return Xavier()
        elif code == 'center':
            return Center()
        else:
            raise ModuleNotFoundError(code)
