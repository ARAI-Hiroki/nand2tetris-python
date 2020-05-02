from unittest import TestCase, main
from src.chap01.xor_gate import XorGate
from tests.chap01.base_clock import TestBaseClock


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
