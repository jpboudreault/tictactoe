from cpu.center import Center
from cpu.first import First
from cpu.random import Random
from cpu.xavier import Xavier


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
