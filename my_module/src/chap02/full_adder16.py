from ..chap01.or_gate import OrGate
from ..chap01.digital_circle import DigitalCircle
from .full_adder import FullAdder


class FullAdder16(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        fa = FullAdder()

        a = i[0]
        b = i[1]

        add01 = fa.clock((a[15], b[15], 0))
        add02 = fa.clock((a[14], b[14], add01[0]))
        add03 = fa.clock((a[13], b[13], add02[0]))
        add04 = fa.clock((a[12], b[12], add03[0]))
        add05 = fa.clock((a[11], b[11], add04[0]))
        add06 = fa.clock((a[10], b[10], add05[0]))
        add07 = fa.clock((a[9], b[9], add06[0]))
        add08 = fa.clock((a[8], b[8], add07[0]))
        add09 = fa.clock((a[7], b[7], add08[0]))
        add10 = fa.clock((a[6], b[6], add09[0]))
        add11 = fa.clock((a[5], b[5], add10[0]))
        add12 = fa.clock((a[4], b[4], add11[0]))
        add13 = fa.clock((a[3], b[3], add12[0]))
        add14 = fa.clock((a[2], b[2], add13[0]))
        add15 = fa.clock((a[1], b[1], add14[0]))
        add16 = fa.clock((a[0], b[0], add15[0]))

        carry = add16[0]

        sum = (add16[1], add15[1], add14[1], add13[1],
               add12[1], add11[1], add10[1], add09[1],
               add08[1], add07[1], add06[1], add05[1],
               add04[1], add03[1], add02[1], add01[1])
        return ((carry,) + sum)
