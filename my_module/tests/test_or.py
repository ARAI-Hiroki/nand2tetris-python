from unittest import TestCase, main
from src.or_gate import OrGate
from tests.base_clock import TestBaseClock


class TestOrGate(TestBaseClock):

    def test(self):
        gate = OrGate()

        patterns = (
            # -- inputs -- -- outputs --
            ((1,     True),  (True,)),
            ((True,     False), (True,)),
            ((False,    True),  (True,)),
            ((False,    False), (False,)),
        )

        self.exec(gate, patterns)
