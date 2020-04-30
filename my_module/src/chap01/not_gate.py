from .nand_gate import NandGate
from .digital_circle import DigitalCircle


class NotGate(DigitalCircle):

    def __init__(self):
        self.nand_gate = NandGate()

    def clock(self, i):
        ng = self.nand_gate

        return ng.clock((i[0], i[0]))
