from functools import reduce
from ..chap01.and_gate import AndGate
from ..chap01.or_gate import OrGate
from ..chap01.not_gate import NotGate
from ..chap01.xor_gate import XorGate
from ..chap01.digital_circle import DigitalCircle
from .half_adder import HalfAdder
from .full_adder16 import FullAdder16


class ALU(DigitalCircle):

    def __init__(self):
        pass

    def clock(self, i):
        ag = AndGate()
        og = OrGate()
        ng = NotGate()
        xo = XorGate()
        adder = FullAdder16()

        x = i[0:16]   # 入力 x
        y = i[16:32]  # 入力 y
        zx = i[32]    # x を 0 にする
        nx = i[33]    # x を反転する
        zy = i[34]    # y を 0 にする
        ny = i[35]    # y を反転する
        f = i[36]     # 1 は加算、 0 は And 演算
        no = i[37]    # 出力 out を反転する

        # zx x   x
        # ---------
        # 0  0   0
        # 0  1   1
        # 1  0   0
        # 1  1   0
        x = tuple(reduce(lambda before, e:
                         before + ag.clock(ng.clock((zx,)) + (e,)), x, ()))

        y = tuple(reduce(lambda before, e:
                         before + ag.clock(ng.clock((zy,)) + (e,)), y, ()))

        # nx x    x
        # ---------
        # 0  0    0
        # 0  1    1
        # 1  0    1
        # 1  1    0
        x = tuple(reduce(lambda before, e: before + xo.clock((nx, e)), x, ()))

        y = tuple(reduce(lambda before, e: before + xo.clock((ny, e)), y, ()))

        tmp = adder.clock((x, y))
        carry = tmp[0]
        add_res = tmp[1:17]

        and_res = tuple(reduce(lambda before, xy:
                               before + ag.clock(xy), tuple(zip(*(x, y))), ()))

        # 加算か乗算かによる結果を取得
        out = tuple(reduce(lambda before, xy:
                           before + og.clock(
                               ag.clock((f, xy[0])) +
                               ag.clock(ng.clock((f,)) + (xy[1],))
                           ),
                           tuple(zip(*(add_res, and_res))), ()))

        #  out  no    out
        # ----------------
        #   0    0     0
        #   0    1     1
        #   1    0     1
        #   1    1     0
        out = tuple(reduce(lambda before, x:
                           before + xo.clock((no, x)), out, ()))

        out_non_zero = tuple(reduce(lambda before, x:
                                    og.clock(before + (x,)), out, (False,)))

        out_zr = ng.clock(out_non_zero)  # out_zr out = 0 の場合にのみ True となる
        out_ng = out[0]                  # out_ng out < 0 の場合にのみ True となる

        return out + out_zr + (out_ng,)
