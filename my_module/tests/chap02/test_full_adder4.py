from unittest import TestCase, main
from src.chap02.full_adder4 import FullAdder4
from tests.chap01.base_clock import TestBaseClock


class TestAdd16(TestBaseClock):

    def test(self):
        gate = FullAdder4()

        patterns = (
            (((0, 0, 0, 0), (0, 0, 0, 0)), (0, 0, 0, 0, 0)),
            (((0, 0, 0, 1), (1, 0, 0, 0)), (0, 1, 0, 0, 1)),
            (((0, 0, 1, 1), (1, 1, 0, 0)), (0, 1, 1, 1, 1)),

            (((1, 0, 1, 1), (0, 0, 0, 0)), (0, 1, 0, 1, 1)),
            (((1, 0, 1, 1), (0, 0, 0, 1)), (0, 1, 1, 0, 0)),
            (((1, 0, 1, 1), (0, 0, 1, 0)), (0, 1, 1, 0, 1)),

            (((1, 1, 1, 1), (0, 0, 0, 1)), (1, 0, 0, 0, 0)),
            (((1, 1, 1, 1), (0, 0, 1, 0)), (1, 0, 0, 0, 1)),
        )

        self.exec(gate, patterns)
