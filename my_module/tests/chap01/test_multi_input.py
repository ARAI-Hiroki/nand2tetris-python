from unittest import TestCase, main
from src.chap01.multi_input import *
from tests.chap01.base_test import BaseTest


class TestBasicGate(BaseTest):

    def test_or8way(self):
        inputs = (
            (0, 0, 0, 0,   0, 0, 0, 0),
            (0, 0, 0, 0,   0, 0, 0, 1),
            (0, 0, 0, 0,   0, 0, 1, 1),
            (0, 0, 0, 0,   0, 1, 1, 1),
            (0, 0, 0, 0,   1, 1, 1, 1),
            (0, 0, 0, 1,   1, 1, 1, 1),
            (0, 0, 1, 1,   1, 1, 1, 1),
            (0, 1, 1, 1,   1, 1, 1, 1),
            (1, 1, 1, 1,   1, 1, 1, 1),
            (1, 1, 1, 1,   1, 1, 1, 1),
            (1, 1, 1, 1,   1, 1, 1, 0),
            (1, 1, 1, 1,   1, 1, 0, 0),
            (1, 1, 1, 1,   1, 0, 0, 0),
            (1, 1, 1, 1,   0, 0, 0, 0),
            (1, 1, 1, 0,   0, 0, 0, 0),
            (1, 1, 0, 0,   0, 0, 0, 0),
            (1, 0, 0, 0,   0, 0, 0, 0),
        )

        expected = (
            (0,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
            (1,),
        )

        self.exec(or8way, inputs, expected)

    def test_mux4way(self):
        inputs = (
            (1, 0, 1, 0,     (0, 0)),
            (1, 0, 1, 0,     (0, 1)),
            (1, 0, 1, 0,     (1, 0)),
            (1, 0, 1, 0,     (1, 1)),
        )

        expected = (
            (1,),
            (0,),
            (1,),
            (0,),
        )

        self.exec(mux4way, inputs, expected)

    def test_mux4way16(self):
        inputs = (
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,     (0, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,     (0, 1)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,     (1, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,     (1, 1)),
        )

        expected = (
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
        )

        self.exec(mux4way16, inputs, expected)

    def test_mux8way16(self):
        inputs = (
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (0, 0, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (0, 0, 1)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (0, 1, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (0, 1, 1)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (1, 0, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (1, 0, 1)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (1, 1, 0)),
            ((1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16,
             (1,) * 16, (0,) * 16, (1,) * 16, (0,) * 16, (1, 1, 1)),
        )

        expected = (
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
            (((1,) * 16),),
            (((0,) * 16),),
        )

        self.exec(mux8way16, inputs, expected)

    def test_dmux4way(self):
        inputs = (
            (1, (0, 0)),
            (0, (0, 0)),
            (1, (0, 1)),
            (0, (0, 1)),
            (1, (1, 0)),
            (0, (1, 0)),
            (1, (1, 1)),
            (0, (1, 1)),
        )

        expected = (
            ((1, 0, 0, 0,),),
            ((0, 0, 0, 0,),),
            ((0, 1, 0, 0,),),
            ((0, 0, 0, 0,),),
            ((0, 0, 1, 0,),),
            ((0, 0, 0, 0,),),
            ((0, 0, 0, 1,),),
            ((0, 0, 0, 0,),),
        )

        self.exec(dmux4way, inputs, expected)

    def test_dmux8way(self):
        inputs = (
            (1, (0, 0, 0)),
            (0, (0, 0, 0)),
            (1, (0, 0, 1)),
            (0, (0, 0, 1)),
            (1, (0, 1, 0)),
            (0, (0, 1, 0)),
            (1, (0, 1, 1)),
            (0, (0, 1, 1)),

            (1, (1, 0, 0)),
            (0, (1, 0, 0)),
            (1, (1, 0, 1)),
            (0, (1, 0, 1)),
            (1, (1, 1, 0)),
            (0, (1, 1, 0)),
            (1, (1, 1, 1)),
            (0, (1, 1, 1)),
        )

        expected = (
            ((1, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 1, 0, 0, 0, 0, 0, 0),),
            ((0, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 0, 1, 0, 0, 0, 0, 0),),
            ((0, 0, 0, 0, 0, 0, 0, 0),),
            ((0, 0, 0, 1, 0, 0, 0, 0),),
            ((0, 0, 0, 0, 0, 0, 0, 0),),

            ((0, 0, 0, 0, 1, 0, 0, 0,),),
            ((0, 0, 0, 0, 0, 0, 0, 0,),),
            ((0, 0, 0, 0, 0, 1, 0, 0,),),
            ((0, 0, 0, 0, 0, 0, 0, 0,),),
            ((0, 0, 0, 0, 0, 0, 1, 0,),),
            ((0, 0, 0, 0, 0, 0, 0, 0,),),
            ((0, 0, 0, 0, 0, 0, 0, 1,),),
            ((0, 0, 0, 0, 0, 0, 0, 0,),),
        )

        self.exec(dmux8way, inputs, expected)
