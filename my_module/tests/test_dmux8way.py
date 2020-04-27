from unittest import TestCase, main
from src.dmux8way import DMux8Way
from tests.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = DMux8Way()

        patterns = (
            # -- inputs --              -- outputs --
            ((0,    0, 0, 0),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    0, 0, 1),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    0, 1, 0),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    0, 1, 1),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    1, 0, 0),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    1, 0, 1),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    1, 1, 0),     (0, 0, 0, 0, 0, 0, 0, 0)),
            ((0,    1, 1, 1),     (0, 0, 0, 0, 0, 0, 0, 0)),

            ((1,    0, 0, 0),     (1, 0, 0, 0, 0, 0, 0, 0)),
            ((1,    0, 0, 1),     (0, 1, 0, 0, 0, 0, 0, 0)),
            ((1,    0, 1, 0),     (0, 0, 1, 0, 0, 0, 0, 0)),
            ((1,    0, 1, 1),     (0, 0, 0, 1, 0, 0, 0, 0)),
            ((1,    1, 0, 0),     (0, 0, 0, 0, 1, 0, 0, 0)),
            ((1,    1, 0, 1),     (0, 0, 0, 0, 0, 1, 0, 0)),
            ((1,    1, 1, 0),     (0, 0, 0, 0, 0, 0, 1, 0)),
            ((1,    1, 1, 1),     (0, 0, 0, 0, 0, 0, 0, 1)),

        )

        self.exec(gate, patterns)