from ..chap01.basic_gate import *
from ..chap01.multi_bit import *
from ..chap01.multi_input import *
from ..chap02.adder import *


def alu(x16, y16, zx, nx, zy, ny, f, no):

    # zx x   x
    # ---------
    # 0  0   0
    # 0  1   1
    # 1  0   0
    # 1  1   0
    x16 = tuple(g_and(x, g_not(zx)) for x in x16)
    y16 = tuple(g_and(y, g_not(zy)) for y in y16)

    # nx x    x
    # ---------
    # 0  0    0
    # 0  1    1
    # 1  0    1
    # 1  1    0
    x16 = tuple(g_xor(x, nx) for x in x16)
    y16 = tuple(g_xor(y, ny) for y in y16)

    add_result = add16(x16, y16)
    and_result = and16(x16, y16)

    #   f      out
    # -------------
    #   0    and_result
    #   1    add_result
    out = mux16(and_result, add_result, f)

    #  out  no    out
    # ----------------
    #   0    0     0
    #   0    1     1
    #   1    0     1
    #   1    1     0
    out = tuple(g_xor(o, no) for o in out)

    # zero flag
    zr = g_not(g_or(or8way(*out[0:8]), or8way(*out[8:16])))

    # negative flag
    ng = out[0]

    return out, zr, ng
