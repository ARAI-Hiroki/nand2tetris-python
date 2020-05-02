from ..chap01.basic_gate import *
from ..chap01.multi_bit import *
from ..chap01.multi_input import *
from functools import reduce


def half_adder(a, b):
    carry = g_and(a, b)
    sum = g_xor(a, b)
    return carry, sum


def full_adder(a, b, c):
    tmp = half_adder(a, b)
    tmp2 = half_adder(c, tmp[1])

    carry = g_or(tmp[0], tmp2[0])
    sum = tmp2[1]

    return carry, sum


def add16(a16, b16):
    sum = []

    carry_before = 0
    for a, b in reversed(tuple(zip(a16, b16))):
        c, s = full_adder(a, b, carry_before)
        sum.append(s)
        carry_before = c

    return tuple(reversed(sum))


def inc16(a16):
    inc = ((0,) * 15 + (1,))
    return add16(a16, inc)
