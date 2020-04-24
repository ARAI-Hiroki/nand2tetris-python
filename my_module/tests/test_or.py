from unittest import TestCase, main
from src.or_gate import OrGate

class TestOrGate(TestCase):

  def test(self):
    gate = OrGate()

    patterns = (
      # -- inputs -- -- outputs --
      ((True, True),    True),
      ((True, False),   True),
      ((False, True),  True),
      ((False, False),  False)
    )

    for input, expected in patterns:
      with self.subTest(input=input, expected=expected):
        actual = gate.clock(input)
        self.assertEqual(expected, actual)
