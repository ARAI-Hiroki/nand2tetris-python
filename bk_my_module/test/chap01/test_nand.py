from unittest import TestCase, main
from src.chap01.nand_gate import NandGate
from tests.chap01.base_clock import TestBaseClock


class TestNandGate(TestBaseClock):

    def test(self):

        gate = NandGate()

        patterns = (
            #  -- inputs --   -- outputs --
            ((True,     True),  (False,)),
            ((True,     False), (True,)),
            ((False,    True),  (True,)),
            ((False,    False), (True,))
        )

        self.exec(gate, patterns)
