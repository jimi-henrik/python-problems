nums = [4,2,6,9]
target = 10

class Selution:
  def __init__(self):
    self.nums = []
    self.target = 0

  def twosum(self, numerolista, vastaus):
    self.nums = numerolista
    self.target = vastaus
    for x in numerolista:
      for y in numerolista:
        if numerolista.index(x) != numerolista.index(y):
          if x + y == vastaus:
            return [numerolista.index(x), numerolista.index(y)]

ratkaisu = Selution()

lista = ratkaisu.twosum(nums, target)

print(lista)