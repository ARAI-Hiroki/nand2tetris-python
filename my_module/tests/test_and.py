from unittest import TestCase, main
from src.and_gate import AndGate
from tests.base_clock import TestBaseClock


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
