from unittest import TestCase, main
from src.chap01.and16_gate import And16Gate
from tests.chap01.base_clock import TestBaseClock


class TestNot16Gate(TestBaseClock):

    def test(self):

        gate = And16Gate()

        patterns = (
            # -- inputs --          -- outputs --
            (((True,   True),) * 16,  (True,) * 16),
            (((True,   False),) * 16, (False,) * 16),
            (((False,  True),) * 16,  (False,) * 16),
            (((False, False),) * 16,  (False,) * 16),

            # 15 個の (False, False) と 1 個の (True, True) を持つ tuple が正しく置換されるかどうか
            (((False,  False),) * 15 + ((True, True),),   (False,) * 15 + (True,)),
        )

        self.exec(gate, patterns)
