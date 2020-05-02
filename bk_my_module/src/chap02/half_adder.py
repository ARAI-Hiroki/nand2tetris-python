from ..chap01.and_gate import AndGate
from ..chap01.xor_gate import XorGate
from ..chap01.digital_circle import DigitalCircle


class HalfAdder(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        ag = AndGate()
        xo = XorGate()

        carry = ag.clock(i)
        sum = xo.clock(i)

        return carry + sum
