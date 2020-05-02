from unittest import TestCase, main
from src.chap01.multi_bit import *
from tests.chap01.base_test import BaseTest


class TestBasicGate(BaseTest):

    def test_not16(self):
        inputs = self.basic_bits['16b1']

        expected = (
            ((0,) * 16,),
            ((1,) * 16,),
        )

        self.exec(not16, inputs, expected)

    def test_and16(self):
        inputs = self.basic_bits['16b2']
        expected = (
            (((0,) * 16),),
            (((0,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
        )

        self.exec(and16, inputs, expected)

    def test_or16(self):
        inputs = inputs = self.basic_bits['16b2']

        expected = (
            (((0,) * 16),),
            (((1,) * 16),),
            (((1,) * 16),),
            (((1,) * 16),),
        )

        self.exec(or16, inputs, expected)

    def test_mux16(self):
        sel = (
            0,
            0,
            0,
            0,
            1,
            1,
            1,
            1,
        )
        inp = self.basic_bits['16b2']
        inputs = self.tuple_join(inp * 2, sel)

        expected = (
            (((0,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
        )
        self.exec(mux16, inputs, expected)
