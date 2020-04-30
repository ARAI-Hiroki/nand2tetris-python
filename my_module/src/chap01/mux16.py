from .digital_circle import DigitalCircle
from .mux import Mux
from functools import reduce


class Mux16(DigitalCircle):

    def __init__(self):
        self.mux = Mux()

    def clock(self, i):
        mu = self.mux
        return reduce(lambda x, y: x + mu.clock((y[0], y[1], y[2])), i, ())
