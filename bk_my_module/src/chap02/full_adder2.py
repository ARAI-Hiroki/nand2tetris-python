from ..chap01.or_gate import OrGate
from ..chap01.digital_circle import DigitalCircle
from .full_adder import FullAdder


class FullAdder2(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        fa = FullAdder()

        a = i[0]
        b = i[1]

        add1 = fa.clock((a[1], b[1], 0))
        add2 = fa.clock((a[0], b[0], add1[0]))

        carry = add2[0]
        sum = (add2[1], add1[1])
        return ((carry,) + sum)
