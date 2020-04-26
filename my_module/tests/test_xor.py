from unittest import TestCase, main
from src.xor_gate import XorGate
from tests.base_clock import TestBaseClock


class TestXorGate(TestBaseClock):

    def test(self):
        gate = XorGate()

        patterns = (
            # -- inputs -- -- outputs --
            ((True,     True),  (False,)),
            ((True,     False), (True,)),
            ((False,    True),  (True,)),
            ((False,    False), (False,)),
        )

        self.exec(gate, patterns)
