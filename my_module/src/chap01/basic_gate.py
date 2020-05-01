def g_nand(a, b):
    return not (a and b)


def g_not(a):
    return g_nand(a, a)


def g_and(a, b):
    return g_nand(
        g_nand(a, b),
        g_nand(a, b)
    )


def g_or(a, b):
    return g_nand(
        g_nand(a, a),
        g_nand(b, b)
    )


def g_xor(a, b):
    return g_nand(
        g_nand(a, g_nand(a, b)),
        g_nand(g_nand(a, b), b)
    )


def mux(a, b, sel):
    return g_or(
        g_and(a, g_not(sel)),
        g_and(b, sel)
    )


def dmux(a, sel):
    return (
        g_and(a, g_not(sel)),
        g_and(a, sel)
    )
