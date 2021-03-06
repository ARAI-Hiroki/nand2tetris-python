from unittest import TestCase, main
from src.chap01.mux8way import Mux8Way
from tests.chap01.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = Mux8Way()

        patterns = (
            # -- inputs --     -- outputs --
            # a  b  c  d  e  f  g  h      sel
            ((1, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0), (1,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  0, 0, 1), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  0, 1, 0), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  0, 1, 1), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  1, 0, 0), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  1, 0, 1), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  1, 1, 0), (0,)),
            ((1, 0, 0, 0, 0, 0, 0, 0,  1, 1, 1), (0,)),

            ((0, 1, 0, 0, 0, 0, 0, 0,  0, 0, 0), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  0, 0, 1), (1,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  0, 1, 0), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  0, 1, 1), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  1, 0, 0), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  1, 0, 1), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  1, 1, 0), (0,)),
            ((0, 1, 0, 0, 0, 0, 0, 0,  1, 1, 1), (0,)),

            ((0, 0, 1, 0, 0, 0, 0, 0,  0, 0, 0), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  0, 0, 1), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  0, 1, 0), (1,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  0, 1, 1), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  1, 0, 0), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  1, 0, 1), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  1, 1, 0), (0,)),
            ((0, 0, 1, 0, 0, 0, 0, 0,  1, 1, 1), (0,)),

            ((0, 0, 0, 1, 0, 0, 0, 0,  0, 0, 0), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  0, 0, 1), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  0, 1, 0), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  0, 1, 1), (1,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  1, 0, 0), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  1, 0, 1), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  1, 1, 0), (0,)),
            ((0, 0, 0, 1, 0, 0, 0, 0,  1, 1, 1), (0,)),

            ((0, 0, 0, 0, 1, 0, 0, 0,  0, 0, 0), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  0, 0, 1), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  0, 1, 0), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  0, 1, 1), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  1, 0, 0), (1,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  1, 0, 1), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  1, 1, 0), (0,)),
            ((0, 0, 0, 0, 1, 0, 0, 0,  1, 1, 1), (0,)),

            ((0, 0, 0, 0, 0, 1, 0, 0,  0, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  0, 0, 1), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  0, 1, 0), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  0, 1, 1), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  1, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  1, 0, 1), (1,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  1, 1, 0), (0,)),
            ((0, 0, 0, 0, 0, 1, 0, 0,  1, 1, 1), (0,)),

            ((0, 0, 0, 0, 0, 0, 1, 0,  0, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  0, 0, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  0, 1, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  0, 1, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  1, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  1, 0, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  1, 1, 0), (1,)),
            ((0, 0, 0, 0, 0, 0, 1, 0,  1, 1, 1), (0,)),

            ((0, 0, 0, 0, 0, 0, 0, 1,  0, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  0, 0, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  0, 1, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  0, 1, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  1, 0, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  1, 0, 1), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  1, 1, 0), (0,)),
            ((0, 0, 0, 0, 0, 0, 0, 1,  1, 1, 1), (1,)),
        )

        self.exec(gate, patterns)
