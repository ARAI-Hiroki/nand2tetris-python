from .basic_gate import *


def not16(a):
    return tuple(g_not(x) for x in a)


def and16(a, b):
    return tuple(g_and(x, y) for x, y in zip(*(a, b)))


def or16(a, b):
    return tuple(g_or(x, y) for x, y in zip(*(a, b)))


def mux16(a, b, sel):
    return tuple(mux(x, y, sel) for x, y in zip(*(a, b)))
