from unittest import TestCase, main
from src.mux4way import Mux4Way
from tests.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = Mux4Way()

        patterns = (
            # -- inputs --     -- outputs --
            # a  b  c  d     sel
            ((1, 0, 0, 0,   0, 0,), (1,)),
            ((1, 0, 0, 0,   0, 1,), (0,)),
            ((1, 0, 0, 0,   1, 0,), (0,)),
            ((1, 0, 0, 0,   1, 1,), (0,)),

            ((1, 1, 1, 0,   0, 0,), (1,)),
            ((1, 1, 1, 0,   0, 1,), (1,)),
            ((1, 1, 1, 0,   1, 0,), (1,)),
            ((1, 1, 1, 0,   1, 1,), (0,)),

            ((0, 1, 1, 1,   0, 0,), (0,)),
            ((0, 1, 1, 1,   0, 1,), (1,)),
            ((0, 1, 1, 1,   1, 0,), (1,)),
            ((0, 1, 1, 1,   1, 1,), (1,)),

            ((0, 0, 0, 1,   0, 0,), (0,)),
            ((0, 0, 0, 1,   0, 1,), (0,)),
            ((0, 0, 0, 1,   1, 0,), (0,)),
            ((0, 0, 0, 1,   1, 1,), (1,)),
        )

        self.exec(gate, patterns)
