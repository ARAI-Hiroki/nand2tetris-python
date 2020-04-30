from unittest import TestCase, main
from src.chap01.not_gate import NotGate
from tests.chap01.base_clock import TestBaseClock


class TestNotGate(TestBaseClock):

    def test(self):

        gate = NotGate()

        patterns = (
            # -- inputs -- -- outputs --
            ((True,),       (False,)),
            ((False,),      (True,))
        )

        self.exec(gate, patterns)
