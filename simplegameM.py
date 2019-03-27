###########################
# hack war robot (c)2018  #
# email cyber1@centrum.sk #
###########################
import random , sys
from math import exp, expm1
from simplegameI import robotgame, get_input

while True:
  weight = 0.0
  if get_input() == None:
       weight = robotgame(weight)