class NandGate:
  def clock(self, i):
    return not (i[0] and i[1])