from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from .digital_circle import DigitalCircle

from functools import reduce


class DMux8Way(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        ng = self.not_gate

        inp = i[0]
        sel = i[1:4]

        fil = ()
        fil += ag.clock(
            ag.clock(ng.clock((sel[0],))
                     + ng.clock((sel[1],)))
            + ng.clock((sel[2],))
        )

        fil += ag.clock(
            ag.clock(ng.clock((sel[0],))
                     + ng.clock((sel[1],)))
            + (sel[2],)
        )

        fil += ag.clock(
            ag.clock(ng.clock((sel[0],))
                     + (sel[1],))
            + ng.clock((sel[2],))
        )

        fil += ag.clock(
            ag.clock(ng.clock((sel[0],))
                     + (sel[1],))
            + (sel[2],)
        )

        fil += ag.clock(
            ag.clock((sel[0],)
                     + ng.clock((sel[1],)))
            + ng.clock((sel[2],))
        )

        fil += ag.clock(
            ag.clock((sel[0],)
                     + ng.clock((sel[1],)))
            + (sel[2],)
        )

        fil += ag.clock(
            ag.clock((sel[0],)
                     + (sel[1],))
            + ng.clock((sel[2],))
        )

        fil += ag.clock(
            ag.clock((sel[0],)
                     + (sel[1],))
            + (sel[2],)
        )

        return tuple(reduce(
            lambda before, x: before + ag.clock((inp, x)),
            fil, ()))
