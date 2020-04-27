from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from .digital_circle import DigitalCircle


class DMux(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        ng = self.not_gate

        return (
            ag.clock((i[0],) + ng.clock((i[1],)))
            + ag.clock((i[0], i[1]))
        )
