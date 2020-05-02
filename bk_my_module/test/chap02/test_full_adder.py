from unittest import TestCase, main
from src.chap02.full_adder import FullAdder
from tests.chap01.base_clock import TestBaseClock


class TestFullAdder(TestBaseClock):

    def test(self):
        gate = FullAdder()

        patterns = (
            #  in            out
            # a  b  c    carry sum
            ((0, 0, 0),    (0, 0)),
            ((0, 0, 1),    (0, 1)),
            ((0, 1, 0),    (0, 1)),
            ((0, 1, 1),    (1, 0)),

            ((1, 0, 0),    (0, 1)),
            ((1, 0, 1),    (1, 0)),
            ((1, 1, 0),    (1, 0)),
            ((1, 1, 1),    (1, 1)),
        )

        self.exec(gate, patterns)
