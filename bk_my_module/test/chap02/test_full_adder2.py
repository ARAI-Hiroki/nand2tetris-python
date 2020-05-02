from unittest import TestCase, main
from src.chap02.full_adder2 import FullAdder2
from tests.chap01.base_clock import TestBaseClock


class TestAdder2(TestBaseClock):

    def test(self):
        gate = FullAdder2()

        patterns = (
            #   a       b    carry sum
            (((0, 0), (0, 0)), (0, 0, 0)),
            # (((0, 0), (0, 1)), (0, 0, 1)),
            # (((0, 0), (1, 0)), (0, 1, 0)),
            # (((0, 0), (1, 1)), (0, 1, 1)),

            # (((0, 1), (0, 0)), (0, 0, 1)),
            # (((0, 1), (0, 1)), (0, 1, 0)),
            # (((0, 1), (1, 0)), (0, 1, 1)),
            # (((0, 1), (1, 1)), (1, 0, 0)),

            # (((1, 0), (0, 0)), (0, 1, 0)),
            # (((1, 0), (0, 1)), (0, 1, 1)),
            # (((1, 0), (1, 0)), (1, 0, 0)),
            # (((1, 0), (1, 1)), (1, 0, 1)),

            # (((1, 1), (0, 0)), (0, 1, 1)),
            # (((1, 1), (0, 1)), (1, 0, 0)),
            # (((1, 1), (1, 0)), (1, 0, 1)),
            # (((1, 1), (1, 1)), (1, 1, 0)),
        )

        self.exec(gate, patterns)
