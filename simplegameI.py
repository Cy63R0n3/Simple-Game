###########################
# hack war robot (c)2018  #
# email cyber1@centrum.sk #
###########################
import random
from math import exp, expm1

def robotgame( weight_before ):
  neuro1 = 1/(1+expm1(random.random()))
  neuro2 = 1/(1+expm1(random.random()))
  neuro3 = 1/(1+expm1(random.random()))
  if neuro1 >= 0.5:
    dist = 1
  else:
    dist = 0
  if neuro2 >= 0.5:
    dist += 2
  else:
    dist += 0
  if neuro3 >= 0.5:
    dist += 4
  else:
    dist += 0	
  print ("#############################")
  print ("## War robots distance:{}".format(dist),"  ##")
  print ("## You:"+dist*"."+"<"+(19-dist)*" "+"##")
  print ("#############################")
  neurol = neuro1+neuro2+neuro3 
  weight = neurol*3
  output = neuro1*weight+neuro2*weight+neuro3*weight  
  print ("-> Neuron output:%29.25f <- "% output)
# precision of adjust is correct at least after two call 'gamebegin' 
  adjust = 0.01*(weight_before-weight)*neurol
  print ("-> Neuron adjust:%29.25f <- "% adjust)
  if neurol > 1.1 and dist == 0:
     print ("- You are not relive war robot -\a \a")
  if neurol < 1.1 and dist == 0:
     print ("** You just hacked war robot **\a")
  return dist, neurol, weight

def get_input():
  print ("Enter command")
  command = input(": ").split()
  verb_word = command[0]
  if verb_word == "gamebegin":
    print ("Game of robots has begun!")
  else:
    print("Unknown verb {}". format(verb_word)," write : gamebegin")
    return verb_word