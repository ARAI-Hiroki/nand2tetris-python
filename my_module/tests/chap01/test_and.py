from unittest import TestCase, main
from src.chap01.and_gate import AndGate
from tests.chap01.base_clock import TestBaseClock


class TestAndGate(TestBaseClock):

    def test(self):

        gate = AndGate()

        patterns = (
            # -- inputs -- -- outputs --
            ((True,     True),  (True,)),
            ((True,     False), (False,)),
            ((False,    True),  (False,)),
            ((False,    False), (False,)),
        )

        self.exec(gate, patterns)
