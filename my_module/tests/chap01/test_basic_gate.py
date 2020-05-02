from unittest import TestCase, main
from src.chap01.basic_gate import *
from tests.chap01.base_test import BaseTest


class TestBasicGate(BaseTest):

    def test_not(self):
        inputs = self.basic_bits['1']

        expected = (
            (1,),
            (0,),
        )

        self.exec(g_not, inputs, expected)

    def test_and(self):

        inputs = self.basic_bits['2']

        expected = (
            (0,),
            (0,),
            (0,),
            (1,),
        )

        self.exec(g_and, inputs, expected)

    def test_or(self):

        inputs = self.basic_bits['2']

        expected = (
            (0,),
            (1,),
            (1,),
            (1,),
        )

        self.exec(g_or, inputs, expected)

    def test_xor(self):

        inputs = self.basic_bits['2']

        expected = (
            (0,),
            (1,),
            (1,),
            (0,),
        )

        self.exec(g_xor, inputs, expected)

    def test_mux(self):
        # a, b, sel
        inputs = self.basic_bits['3']

        expected = (
            (0,),
            (0,),
            (0,),
            (1,),
            (1,),
            (0,),
            (1,),
            (1,),
        )

        self.exec(mux, inputs, expected)

    def test_dmux(self):

        # a, sel
        inputs = self.basic_bits['2']

        expected = (
            (0, 0),
            (0, 0),
            (1, 0),
            (0, 1),
        )
