from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from .digital_circle import DigitalCircle


class Mux(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def clock(self, i):
        a = i[0]
        b = i[1]
        sel = i[2]

        ag = self.and_gate
        og = self.or_gate
        ng = self.not_gate

        return og.clock(
            ag.clock(((a,) + ng.clock((sel,)))) +
            ag.clock((b, sel))
        )
