class Dff:

    before = 0

    def clock(self, p):

        self.before, p = p, self.before

        return p

