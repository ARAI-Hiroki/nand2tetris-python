from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from .digital_circle import DigitalCircle

from functools import reduce


class Mux4Way(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        og = self.or_gate
        ng = self.not_gate

        inp = i[0:4]
        sel = i[4:6]

        fil = (
            ag.clock(ng.clock((sel[0],)) + ng.clock((sel[1],))) +
            ag.clock(ng.clock((sel[0],)) + (sel[1],)) +
            ag.clock((sel[0],) + ng.clock((sel[1],))) +
            ag.clock((sel[0], sel[1]))
        )

        return reduce(
            lambda before, index:
                og.clock(before + ag.clock((inp[index], fil[index]))),
            range(4), (False,))
