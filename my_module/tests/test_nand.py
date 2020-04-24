from unittest import TestCase, main
from src.nand import Nand

class TestNand(TestCase):

  def test_nand(self):
    nand = Nand()

    patterns = (
      ((True, True),    False),
      ((True, False),   True),
      ((False, False),  True),
      ((False, False),  True)
    )

    for input, actual in patterns:
      expected = nand.clock(input)
      self.assertEqual(expected, actual)
