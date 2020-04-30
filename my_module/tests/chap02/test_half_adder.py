from unittest import TestCase, main
from src.chap02.half_adder import HalfAdder
from tests.chap01.base_clock import TestBaseClock


class TestHalfAdder(TestBaseClock):

    def test(self):
        gate = HalfAdder()

        patterns = (
            #  in         out
            # a  b    carry sum
            ((0, 0),    (0, 0)),
            ((0, 1),    (0, 1)),
            ((1, 0),    (0, 1)),
            ((1, 1),    (1, 0)),
        )

        self.exec(gate, patterns)
