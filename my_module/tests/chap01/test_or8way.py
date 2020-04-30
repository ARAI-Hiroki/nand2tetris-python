from unittest import TestCase, main
from src.chap01.or8way import Or8Way
from tests.chap01.base_clock import TestBaseClock


class TestOr8Way(TestBaseClock):

    def test(self):

        gate = Or8Way()

        patterns = (
            ((True,) * 8,             (True,)),
            ((True,) * 7 + (False,),  (True,)),
            ((False,) + (True,) * 7,  (True,)),
            ((False,) * 7 + (True,),  (True,)),
            ((True,) + (False,) * 7,  (True,)),
            ((False,) * 8,            (False,)),
        )

        self.exec(gate, patterns)
