from unittest import TestCase, main
from src.not_gate import NotGate

class TestNotGate(TestCase):

  def test(self):
    gate = NotGate()

    patterns = (
        # -- inputs -- -- outputs --
        ((True,),       False),
        ((False,),      True)
    )

    for input, expected in patterns:
      with self.subTest(input=input, expected=expected):
        actual = gate.clock(input)
        self.assertEqual(expected, actual)
