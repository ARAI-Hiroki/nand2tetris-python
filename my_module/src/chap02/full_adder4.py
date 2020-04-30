from ..chap01.or_gate import OrGate
from ..chap01.digital_circle import DigitalCircle
from .full_adder import FullAdder


class FullAdder4(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        fa = FullAdder()

        a = i[0]
        b = i[1]

        add1 = fa.clock((a[3], b[3], 0))
        add2 = fa.clock((a[2], b[2], add1[0]))
        add3 = fa.clock((a[1], b[1], add2[0]))
        add4 = fa.clock((a[0], b[0], add3[0]))

        carry = add4[0]
        sum = (add4[1], add3[1], add2[1], add1[1])

        return ((carry,) + sum)
