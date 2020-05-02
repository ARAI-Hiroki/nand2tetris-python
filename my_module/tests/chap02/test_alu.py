from unittest import TestCase, main
from src.chap02.alu import *
from tests.chap01.base_test import BaseTest


class TestBasicGate(BaseTest):

    default_ab = ((1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1),  # a
                  (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1))  # b

    val_zero = (1, 0, 1, 0, 1, 0)
    val_one = (1, 1, 1, 1, 1, 1)
    val_minus_one = (1, 1, 1, 0, 1, 0)
    raw_x = (0, 0, 1, 1, 0, 0)
    raw_y = (1, 1, 0, 0, 0, 0)
    not_x = (0, 0, 1, 1, 0, 1)
    not_y = (1, 1, 0, 0, 0, 1)
    minus_x = (0, 0, 1, 1, 1, 1)
    minus_y = (1, 1, 0, 0, 0, 1)
    inc_x = (0, 1, 1, 1, 1, 1)
    inc_y = (1, 1, 0, 1, 1, 1)
    plus = (0, 0, 0, 0, 1, 0)
    minus = (0, 1, 0, 0, 1, 1)
    minus_reverse = (0, 0, 0, 1, 1, 1)
    logical_and = (0, 0, 0, 0, 0, 0)
    logical_sum = (0, 1, 0, 1, 0, 1)

    def test_alu_val_one(self):
        inputs = ((self.default_ab + (self.val_one)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_val_zero(self):
        inputs = ((self.default_ab + (self.val_zero)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_val_minux_one(self):
        inputs = ((self.default_ab + (self.val_minus_one)),)
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1), 0, 1),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_raw_x(self):
        inputs = ((self.default_ab + (self.raw_x)),)
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1,  1, 1, 1, 1, 1, 1, 1, 1), 0, 1),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_raw_y(self):
        inputs = ((self.default_ab + (self.raw_y)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_not_x(self):
        inputs = ((self.default_ab + (self.not_x)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0), 1, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_not_y(self):
        inputs = ((self.default_ab + (self.not_y)),)
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0), 0, 1),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_minus_x(self):
        inputs = ((self.default_ab + (self.minus_x)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_minus_y(self):
        inputs = ((self.default_ab + (self.minus_y)),)
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0), 0, 1),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_inc_x(self):
        inputs = ((self.default_ab + (self.inc_x)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 1, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_inc_y(self):
        inputs = ((self.default_ab + (self.inc_y)),)
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 1, 0), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_plus(self):
        inputs = ((self.default_ab + (self.plus),))
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 0), 1, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_minus(self):
        inputs = ((self.default_ab + (self.minus),))
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 0), 0, 1),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_minus_reverse(self):
        inputs = ((self.default_ab + (self.minus_reverse),))
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 1, 0), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_logical_and(self):
        inputs = ((self.default_ab + (self.logical_and),))
        expected = (
            (((0, 0, 0, 0, 0, 0, 0, 0,     0, 0, 0, 0, 0, 0, 0, 1), 0, 0),),
        )

        self.exec(alu, inputs, expected)

    def test_alu_logical_sum(self):
        inputs = ((self.default_ab + (self.logical_sum),))
        expected = (
            (((1, 1, 1, 1, 1, 1, 1, 1,     1, 1, 1, 1, 1, 1, 1, 1), 0, 1),),
        )

        self.exec(alu, inputs, expected)
