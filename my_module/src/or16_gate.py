from .digital_circle import DigitalCircle
from .or_gate import OrGate
from functools import reduce


class Or16Gate(DigitalCircle):

    def __init__(self):
        self.or_gate = OrGate()

    def clock(self, i):
        ag = self.or_gate
        return reduce(lambda x, y: x + ag.clock((y[0], y[1])), i, ())
