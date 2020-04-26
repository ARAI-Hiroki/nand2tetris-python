from .digital_circle import DigitalCircle
from .mux import Mux
from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from functools import reduce


class Mux4Way16(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        og = self.or_gate
        ng = self.not_gate
        mu = self.mux
        return (
            ag.clock(i[0], ag.clock()),
            ag.clock(i[0], ),
            ag.clock(i[0], ),
            ag.clock(i[0], ),
        )
