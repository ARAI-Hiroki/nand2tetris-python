from unittest import TestCase, main
from src.nand_gate import NandGate

class TestNandGate(TestCase):

  def test(self):
    gate = NandGate()

    patterns = (
      # -- inputs -- -- outputs --
      ((True, True),    False),
      ((True, False),   True),
      ((False, True),  True),
      ((False, False),  True)
    )

    for input, expected in patterns:
      with self.subTest(input=input, expected=expected):
        actual = gate.clock(input)
        self.assertEqual(expected, actual)
