from unittest import TestCase, main
from src.chap02.add16 import Add16
from tests.chap01.base_clock import TestBaseClock


class TestAdd16(TestBaseClock):

    def test(self):
        gate = Add16()

        patterns = (
            #  in                      out
            # a             b       carry sum
            (((0,) * 16, (0,) * 16),  ((0,) * 16, (0,) * 16)),
            (((0,) * 16, (1,) * 16),  ((0,) * 16, (1,) * 16)),
            (((1,) * 16, (0,) * 16),  ((0,) * 16, (1,) * 16)),
            (((1,) * 16, (1,) * 16), ((1,) * 16, (0,) * 16)),

            (((1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0), (0,) * 16),
             ((0,) * 16,
              (1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0)))
        )

        self.exec(gate, patterns)
