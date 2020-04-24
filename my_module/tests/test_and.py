from unittest import TestCase, main
from src.and_gate import AndGate

class TestAndGate(TestCase):

  def test(self):
    gate = AndGate()

    patterns = (
      # -- inputs -- -- outputs --
      ((True, True),    True),
      ((True, False),   False),
      ((False, True),  False),
      ((False, False),  False)
    )

    for input, expected in patterns:
      with self.subTest(input=input, expected=expected):
        actual = gate.clock(input)
        self.assertEqual(expected, actual)
