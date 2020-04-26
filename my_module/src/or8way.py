from .digital_circle import DigitalCircle
from .or_gate import OrGate
from functools import reduce


class Or8Way(DigitalCircle):

    def __init__(self):
        self.or_gate = OrGate()

    def clock(self, i):
        og = self.or_gate
        return reduce(lambda x, y: og.clock(x + (y,)), i, (False,))
