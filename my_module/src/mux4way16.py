from .digital_circle import DigitalCircle
from .mux import Mux
from .and_gate import AndGate
from .or_gate import OrGate
from .not_gate import NotGate
from functools import reduce


class Mux4Way16(DigitalCircle):

    def __init__(self):
        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def clock(self, i):

        ag = self.and_gate
        og = self.or_gate
        ng = self.not_gate

        selector = (
            ag.clock(ng.clock((i[4],)) + ng.clock((i[5],))),
            ag.clock(ng.clock((i[4],)) + (i[5],)),
            ag.clock((i[4],) + ng.clock((i[5],))),
            ag.clock((i[4],) + (i[5],)),
        )

        a = tuple(map(lambda x: ag.clock((x,) + selector[0]), i[0]))
        b = tuple(map(lambda x: ag.clock((x,) + selector[1]), i[1]))
        c = tuple(map(lambda x: ag.clock((x,) + selector[2]), i[2]))
        d = tuple(map(lambda x: ag.clock((x,) + selector[3]), i[3]))

        # TODO [0] を使わずに書きたいなあ…
        return tuple(map(lambda x:
                         og.clock(
                             og.clock(a[x] + b[x]) +
                             og.clock(c[x] + d[x])
                         )[0],
                         list(range(16))))
