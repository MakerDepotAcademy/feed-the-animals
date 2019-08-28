from itertools import cycle
from random import sample

class Hole():

  def __init__(self, board, detect, display):
    self._detect = detect
    self._display = display
    self._board = board

  def light(self):
    self._board.setInput(self._detect)
    self._board.turnOn(self._display)

  def reset(self):
    self._board.turnOff(self._display)

class HoleManager(): # Pimp

  def __init__(self, board, holes=15):
    self._board = board
    pin = iter(range(32))
    self.holes = []
    self.the_chosen_ones = []
    for i in range(holes):
      self.holes += [Hole(board, next(pin), next(pin))]

  def run(self):
    self._board.run()

  def select(self, count=5):
    for t in sample(self.holes, count):
      self.the_chosen_ones += [t]
      t.light()
      print(t._detect)
    self.run()

  def awaitHit(self, timeout=30):
    return self._board.awaitChange([i._detect for i in self.the_chosen_ones], timeout)

  def reset(self):
    [i.reset() for i in self.the_chosen_ones]
    self.the_chosen_ones = []
