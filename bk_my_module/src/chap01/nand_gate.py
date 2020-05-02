from .digital_circle import DigitalCircle


def g_nand(self, a, b):
    return not (a and b)


# class NandGate(DigitalCircle):
#     def clock(self, i):
#         out = not (i[0] and i[1])
#         return (out,)
