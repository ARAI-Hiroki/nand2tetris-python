from .digital_circle import DigitalCircle


class NandGate(DigitalCircle):
    def clock(self, i):
        out = not (i[0] and i[1])
        return (out,)
