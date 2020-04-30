from .nand_gate import NandGate
from .digital_circle import DigitalCircle
from .not_gate import NotGate
from functools import reduce


class Not16Gate(DigitalCircle):

    def __init__(self):
        self.not_gate = NotGate()

    def clock(self, i):
        ng = self.not_gate
        return reduce(lambda x, y: x + ng.clock((y,)), i, ())
