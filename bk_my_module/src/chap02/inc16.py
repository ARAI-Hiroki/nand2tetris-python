from ..chap01.or_gate import OrGate
from ..chap01.digital_circle import DigitalCircle
from .half_adder import HalfAdder
from functools import reduce


class Inc16(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        ha = HalfAdder()

        inc = (i,  ((1,) * 16))

        tmp = reduce(lambda before, x:
                     before + (ha.clock(x),), zip(*inc), ())

        return tuple(zip(*tmp))
