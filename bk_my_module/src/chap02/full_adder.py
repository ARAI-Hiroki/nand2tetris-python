from ..chap01.or_gate import OrGate
from ..chap01.digital_circle import DigitalCircle
from .half_adder import HalfAdder


class FullAdder(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        ha = HalfAdder()
        og = OrGate()

        tmp = ha.clock(i[0:2])
        tmp2 = ha.clock((i[2], tmp[1]))

        carry = og.clock((tmp[0], tmp2[0]))
        sum = tmp2[1]

        return (carry + (sum,))
