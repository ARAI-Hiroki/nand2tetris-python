from .nand_gate import NandGate
from .digital_circle import DigitalCircle
from .and_gate import AndGate
from functools import reduce


class And16Gate(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()

    def clock(self, i):
        ag = self.and_gate
        return reduce(lambda x, y: x + ag.clock((y[0], y[1])), i, ())
