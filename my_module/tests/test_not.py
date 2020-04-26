from unittest import TestCase, main
from src.not_gate import NotGate
from tests.base_clock import TestBaseClock


class TestNotGate(TestBaseClock):

    def test(self):

        gate = NotGate()

        patterns = (
            # -- inputs -- -- outputs --
            ((True,),       (False,)),
            ((False,),      (True,))
        )

        self.exec(gate, patterns)
