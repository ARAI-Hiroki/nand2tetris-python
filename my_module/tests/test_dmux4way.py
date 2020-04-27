from unittest import TestCase, main
from src.dmux4way import DMux4Way
from tests.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = DMux4Way()

        patterns = (
            # -- inputs --  -- outputs --
            ((1, 0, 0),     (1, 0, 0, 0)),
            ((1, 0, 1),     (0, 1, 0, 0)),
            ((1, 1, 0),     (0, 0, 1, 0)),
            ((1, 1, 1),     (0, 0, 0, 1)),

            ((0, 0, 0),     (0, 0, 0, 0)),
            ((0, 0, 1),     (0, 0, 0, 0)),
            ((0, 1, 0),     (0, 0, 0, 0)),
            ((0, 1, 1),     (0, 0, 0, 0)),
        )

        self.exec(gate, patterns)
