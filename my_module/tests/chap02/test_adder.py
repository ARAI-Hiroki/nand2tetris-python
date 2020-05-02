from unittest import TestCase, main
from src.chap02.adder import *
from tests.chap01.base_test import BaseTest


class TestBasicGate(BaseTest):

    def test_half_adder(self):
        inputs = self.basic_bits['2']
        expected = (
            ((0, 0),),
            ((0, 1),),
            ((0, 1),),
            ((1, 0),),
        )

        self.exec(half_adder, inputs, expected)

    def test_full_adder(self):
        inputs = self.basic_bits['3']
        expected = (
            ((0, 0),),
            ((0, 1),),
            ((0, 1),),
            ((1, 0),),
            ((0, 1),),
            ((1, 0),),
            ((1, 0),),
            ((1, 1),),
        )

        self.exec(full_adder, inputs, expected)

    def test_add16(self):
        inputs = (
            ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)),

            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)),

            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0),
             (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)),
        )

        expected = (
            ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),),
            ((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0),),
        )

        self.exec(add16, inputs, expected)

    def test_inc16(self):
        inputs = (
            ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),),

            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),),

            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0),),
        )

        expected = (
            ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),),
            ((1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1),),
        )

        self.exec(inc16, inputs, expected)
