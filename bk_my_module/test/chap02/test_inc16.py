from unittest import TestCase, main
from src.chap02.inc16 import Inc16
from tests.chap01.base_clock import TestBaseClock


class TestAdd16(TestBaseClock):

    def test(self):
        gate = Inc16()

        patterns = (
            #  in                      out
            # a               carry sum
            ((0,) * 16,   ((0,) * 16, (1,) * 16)),
            ((1,) * 16,   ((1,) * 16, (0,) * 16)),

            ((1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0),
             ((1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0),
              (0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1))),
        )

        self.exec(gate, patterns)
