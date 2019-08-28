#!/usr/bin/env python
from hole import HoleManager
from lib import Manager
from time import sleep

Score = 0

M = Manager()
B = next(iter(M))
H = HoleManager(B)
H.reset()

while True:
  H.select()
  if H.awaitHit():
    Score += 1
  H.reset()
