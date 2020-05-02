from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from .digital_circle import DigitalCircle

from functools import reduce


class DMux4Way(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        ng = self.not_gate

        inp = i[0]
        sel = i[1:3]

        out = (
            ag.clock(ng.clock((sel[0],)) + ng.clock((sel[1],))) +
            ag.clock(ng.clock((sel[0],)) + (sel[1],)) +
            ag.clock((sel[0],) + ng.clock((sel[1],))) +
            ag.clock((sel[0], sel[1]))
        )

        return tuple(reduce(
            lambda before, x: before + ag.clock((inp, x)),
            out, ()))
