from unittest import TestCase, main
from src.chap01.dmux import DMux
from tests.chap01.base_clock import TestBaseClock


class TestMux(TestBaseClock):

    def test(self):

        gate = DMux()

        patterns = (
            # -- inputs --      -- outputs --
            ((True,   True),   (False,  True)),
            ((True,   False),  (True,   False)),
            ((False,  True),   (False,  False)),
            ((False,  False),  (False,  False)),
        )

        self.exec(gate, patterns)
