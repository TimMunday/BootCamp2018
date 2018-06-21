# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 09:45:20 2018

@author: Tim
"""

# lab 3

#Problem 1

from object_oriented import Backpack

def test_backpack():
    testpack = Backpack('Barry', 'black', max_size=3)
    if testpack.name != 'Barry':
        print('Backpack.name assigned incorrectly')
    if testpack.color != 'black':
        print('Backpack.color assigned incorrectly')
    if testpack.max_size != 3:
        print('Backpack.max_size assigned incorrectly')
    testpack.put('pens')
    if testpack.contents != ['pens']:
        print('Backpack.put does not work')
    testpack.take('pens')
    if testpack.contents != []:
        print('Backpack.take does not work')
    

        
        my_backpack = Backpack('Fred', 'Blue', max_size=4)

my_backpack.put('a')
my_backpack.put('b')

print(my_backpack.contents)

my_backpack.dump()