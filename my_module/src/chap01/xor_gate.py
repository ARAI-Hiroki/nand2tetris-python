from .nand_gate import NandGate
from .digital_circle import DigitalCircle


class XorGate(DigitalCircle):

    def __init__(self):
        self.nand_gate = NandGate()

    def clock(self, i):
        ng = self.nand_gate
        tmp = ng.clock((i[0], i[1]))
        return ng.clock(
            ng.clock(((i[0],) + tmp)) +
            ng.clock((tmp + (i[1],)))
        )
