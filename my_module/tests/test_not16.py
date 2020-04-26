from unittest import TestCase, main
from src.not16_gate import Not16Gate
from tests.base_clock import TestBaseClock


class TestNot16Gate(TestBaseClock):

    def test(self):

        gate = Not16Gate()

        patterns = (
            # -- inputs --              -- outputs --
            ((True,) * 16,             (False,) * 16),
            ((False,) * 16,            (True,) * 16),
            ((True,) * 15 + (False,),  (False,) * 15 + (True,)),
        )

        self.exec(gate, patterns)
