from unittest import TestCase, main
from src.chap01.mux import Mux
from tests.chap01.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = Mux()

        patterns = (
            # -- inputs --     -- outputs --
            ((True,   True,   True),  (True,)),
            ((True,   False,  True),  (False,)),
            ((False,  True,   True),  (True,)),
            ((False,  False,  True),  (False,)),
            ((True,   True,   False), (True,)),
            ((True,   False,  False), (True,)),
            ((False,  True,   False), (False,)),
            ((False,  False,  False), (False,)),
        )

        self.exec(gate, patterns)
