# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 13:18:16 2018

@author: Tim
"""

import time
import box
import sys
import random as rnd

#Initial numbers
numbers_remain = list(range(1, 10))

#Start of game
if len(sys.argv) == 3:
    #go to game
else:
    print("You need three arguments to start the game')


if sum(numbers_remain <= 6):
    roll = rnd.randint(1, 6)
else:
    roll = rnd.randint(1, 6) + rnd.randint(1, 6)

if isvalid(roll, numbers_remain) == False:
    print('Game over')
    quit()

print(roll)
print('Numbers left = ', numbers_remain)
print('Time left')
player_input = input('Numbers to eliminate:')

player_input_list = parse_input(player_input, numbers_remain)

for i in 1:len(player_input_list):
    numbers_remain.remove(player_input_list[i-1])
    

print(sys.argv[2]) #Print user first guess



numbers = list(range(1, 10))
print('Numbers left = ', numbers)

