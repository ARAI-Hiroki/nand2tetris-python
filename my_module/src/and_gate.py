from .nand_gate import NandGate

class AndGate:

  def __init__(self):
    self.nand_gate = NandGate()

  def clock(self, i):
    ng = self.nand_gate
    
    return ng.clock((
      ng.clock((i[0], i[1])),
      ng.clock((i[0], i[1]))
    ))
