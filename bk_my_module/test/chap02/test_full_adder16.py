from unittest import TestCase, main
from src.chap02.full_adder16 import FullAdder16
from tests.chap01.base_clock import TestBaseClock


class TestAdd16(TestBaseClock):

    def test(self):
        gate = FullAdder16()

        patterns = (
            (((1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1),
              (0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 1)),
             (1,     0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0)),

        )

        self.exec(gate, patterns)
