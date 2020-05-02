from unittest import TestCase, main
from src.chap02.alu import ALU
from tests.chap01.base_clock import TestBaseClock


class TestALU(TestBaseClock):

    def test(self):
        gate = ALU()

        default_ab = (1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1,  # a
                      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)  # b

        val_zero = (1, 0, 1, 0, 1, 0)
        val_one = (1, 1, 1, 1, 1, 1)
        val_minus_one = (1, 1, 1, 0, 1, 0)
        raw_x = (0, 0, 1, 1, 0, 0)
        raw_y = (1, 1, 0, 0, 0, 0)
        not_x = (0, 0, 1, 1, 0, 1)
        not_y = (1, 1, 0, 0, 0, 1)
        minus_x = (0, 0, 1, 1, 1, 1)
        minus_y = (1, 1, 0, 0, 0, 1)
        inc_x = (0, 1, 1, 1, 1, 1)
        inc_y = (1, 1, 0, 1, 1, 1)
        plus = (0, 0, 0, 0, 1, 0)
        minus = (0, 1, 0, 0, 1, 1)
        minus_reverse = (0, 0, 0, 1, 1, 1)
        logical_and = (0, 0, 0, 0, 0, 0)
        logical_sum = (0, 1, 0, 1, 0, 1)

        patterns = (
            (default_ab + val_zero,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0,    1, 0)),

            (default_ab + val_one,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1,    0, 0)),

            (default_ab + val_minus_one,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 1,    0, 1)),

            (default_ab + raw_x,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 1,    0, 1)),  # a は最上位 bit が 1 なので負数だった

            (default_ab + raw_y,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1,    0, 0)),

            (default_ab + not_x,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0,    1, 0)),

            (default_ab + not_y,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0,    0, 1)),

            (default_ab + not_y,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0,    0, 1)),

            (default_ab + minus_x,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1,    0, 0)),

            (default_ab + minus_y,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0,    0, 1)),

            (default_ab + inc_x,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0,    1, 0)),

            (default_ab + inc_y,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 1, 0,    0, 0)),

            (default_ab + plus,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0,    1, 0)),

            (default_ab + minus,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0,    0, 1)),

            (default_ab + minus_reverse,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 1, 0,    0, 0)),

            (default_ab + logical_and,
             (0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1,    0, 0)),

            (default_ab + logical_sum,
             (1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 1,    0, 1)),

        )

        self.exec(gate, patterns)
