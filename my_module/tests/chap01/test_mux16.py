from unittest import TestCase, main
from src.chap01.mux16 import Mux16
from tests.chap01.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = Mux16()

        patterns = (
            # -- inputs --                    -- outputs --
            (((True,   True,   True),) * 16,  (True,) * 16),
            (((True,   False,  True),) * 16,  (False,) * 16),
            (((False,  True,   True),) * 16,  (True,) * 16),
            (((False,  False,  True),) * 16,  (False,) * 16),
            (((True,   True,   False),) * 16, (True,) * 16),
            (((True,   False,  False),) * 16, (True,) * 16),
            (((False,  True,   False),) * 16, (False,) * 16),
            (((False,  False,  False),) * 16, (False,) * 16),
        )

        self.exec(gate, patterns)
