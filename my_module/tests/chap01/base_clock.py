from unittest import TestCase, main
from src.chap01.digital_circle import DigitalCircle


class TestBaseClock(TestCase):

    def exec(self, circle: DigitalCircle, patterns: tuple):

        for input, expected in patterns:
            with self.subTest(input=input, expected=expected):
                actual = circle.clock(input)
                self.assertEqual(expected, actual)
