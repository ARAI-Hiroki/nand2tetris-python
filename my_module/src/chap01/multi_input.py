from .basic_gate import *
from .multi_bit import *
from functools import reduce


def or8way(a, b, c, d, e, f, g, h):
    args = (a, b, c, d, e, f, g, h)
    return reduce(lambda before, x: g_or(before, x), args, False)


def mux4way(a, b, c, d, sel):
    args = (a, b, c, d)
    sel_tmp = (
        g_and(g_not(sel[0]), g_not(sel[1])),
        g_and(g_not(sel[0]), sel[1]),
        g_and(sel[0], g_not(sel[1])),
        g_and(sel[0], sel[1]),
    )
    muxed = tuple(g_and(x, s) for x, s in tuple(zip(args, sel_tmp)))
    return reduce(lambda before, x: g_or(before, x), muxed, False)


def mux4way16(a, b, c, d, sel):
    args = (a, b, c, d)
    return tuple(mux4way(*args_ele, sel) for args_ele in zip(*args))


def mux8way(a, b, c, d, e, f, g, h, sel):
    args = (a, b, c, d, e, f, g, h)
    sel_tmp = (
        g_and(g_not(sel[0]), g_and(g_not(sel[1]), g_not(sel[2]))),
        g_and(g_not(sel[0]), g_and(g_not(sel[1]), sel[2])),
        g_and(g_not(sel[0]), g_and(sel[1],        g_not(sel[2]))),
        g_and(g_not(sel[0]), g_and(sel[1],        sel[2])),
        g_and(sel[0],        g_and(g_not(sel[1]), g_not(sel[2]))),
        g_and(sel[0],        g_and(g_not(sel[1]), sel[2])),
        g_and(sel[0],        g_and(sel[1],        g_not(sel[2]))),
        g_and(sel[0],        g_and(sel[1],        sel[2])),
    )
    muxed = tuple(g_and(x, s) for x, s in tuple(zip(args, sel_tmp)))
    return reduce(lambda before, x: g_or(before, x), muxed, False)


def mux8way16(a, b, c, d, e, f, g, h, sel):
    args = (a, b, c, d, e, f, g, h)
    return tuple(mux8way(*args_ele, sel) for args_ele in zip(*args))


def dmux4way(a, sel):
    sel_tmp = (
        g_and(g_not(sel[0]), g_not(sel[1])),
        g_and(g_not(sel[0]), sel[1]),
        g_and(sel[0], g_not(sel[1])),
        g_and(sel[0], sel[1]),
    )
    return tuple(g_and(a, s) for s in sel_tmp)


def dmux8way(a, sel):
    sel_tmp = (
        g_and(g_not(sel[0]), g_and(g_not(sel[1]), g_not(sel[2]))),
        g_and(g_not(sel[0]), g_and(g_not(sel[1]), sel[2])),
        g_and(g_not(sel[0]), g_and(sel[1],        g_not(sel[2]))),
        g_and(g_not(sel[0]), g_and(sel[1],        sel[2])),
        g_and(sel[0],        g_and(g_not(sel[1]), g_not(sel[2]))),
        g_and(sel[0],        g_and(g_not(sel[1]), sel[2])),
        g_and(sel[0],        g_and(sel[1],        g_not(sel[2]))),
        g_and(sel[0],        g_and(sel[1],        sel[2])),
    )
    return tuple(g_and(a, s) for s in sel_tmp)
