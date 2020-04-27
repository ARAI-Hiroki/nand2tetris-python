from .digital_circle import DigitalCircle
from .mux8way import Mux8Way
from functools import reduce


class Mux8Way16(DigitalCircle):

    def __init__(self):
        self.mux8 = Mux8Way()

    def clock(self, i):

        mu = self.mux8

        inp = i[0:8]
        sel = i[8:11]

        inputs = tuple(zip(*inp))

        return tuple(reduce(
            lambda before, inp: before + mu.clock(inp + sel),
            inputs, ())
        )
