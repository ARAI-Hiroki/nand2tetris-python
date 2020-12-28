import unittest
from src.chap03.dff import *


class TestDff(unittest.TestCase):
    def setUp(self) -> None:
        self.dff = Dff()

    def test_something(self):
        dff = self.dff

        expected = (
            0,
            1,
        )

        result = (
            dff.clock(1),
            dff.clock(1)
        )

        self.assertTupleEqual(expected, result)

