from .digital_circle import DigitalCircle
from .mux4way import Mux4Way
from functools import reduce


class Mux4Way16(DigitalCircle):

    def __init__(self):
        self.mux4 = Mux4Way()

    def clock(self, i):

        mu = self.mux4

        inp = i[0:4]
        sel = i[4:6]

        inputs = tuple(zip(*inp))

        return tuple(reduce(
            lambda before, inp: before + mu.clock(inp + sel),
            inputs, ())
        )
