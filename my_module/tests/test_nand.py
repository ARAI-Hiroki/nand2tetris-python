from unittest import TestCase, main
from src.g_nand import GNand

class TestNand(TestCase):

  def test_nand(self):
    gNand = GNand()

    patterns = (
      # -- inputs -- -- outputs --
      ((True, True),    False),
      ((True, False),   True),
      ((False, False),  True),
      ((False, False),  True)
    )

    for input, actual in patterns:
      expected = gNand.clock(input)
      self.assertEqual(expected, actual)
