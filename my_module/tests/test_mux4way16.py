from unittest import TestCase, main
from src.mux4way16 import Mux4Way16
from tests.base_clock import TestBaseClock


class TestMux8Way(TestBaseClock):

    def test(self):

        gate = Mux4Way16()

        patterns = (
            #             ----- input -----                    ----- output -----
            #    a          b          c          d         sel
            (((0,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    0, 0),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    0, 1),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    1, 0),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    1, 1),   (0,) * 16),

            (((1,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    0, 0),   (1,) * 16),
            (((1,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    0, 1),   (0,) * 16),
            (((1,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    1, 0),   (0,) * 16),
            (((1,) * 16, (0,) * 16, (0,) * 16, (0,) * 16,    1, 1),   (0,) * 16),

            (((1,) * 16, (1,) * 16, (1,) * 16, (0,) * 16,    0, 0),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (0,) * 16,    0, 1),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (0,) * 16,    1, 0),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (0,) * 16,    1, 1),   (0,) * 16),

            (((0,) * 16, (0,) * 16, (0,) * 16, (1,) * 16,    0, 0),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (1,) * 16,    0, 1),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (1,) * 16,    1, 0),   (0,) * 16),
            (((0,) * 16, (0,) * 16, (0,) * 16, (1,) * 16,    1, 1),   (1,) * 16),

            (((1,) * 16, (1,) * 16, (1,) * 16, (1,) * 16,    1, 0),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (1,) * 16,    1, 0),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (1,) * 16,    1, 1),   (1,) * 16),
            (((1,) * 16, (1,) * 16, (1,) * 16, (1,) * 16,    1, 1),   (1,) * 16),
        )

        self.exec(gate, patterns)
