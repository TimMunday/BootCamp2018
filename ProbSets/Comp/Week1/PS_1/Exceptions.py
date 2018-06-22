# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:14:52 2018

@author: Tim
"""

#IO / Exceptions

#Problem 1

def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last "
                   "digits differ by 2 or more: ")
    if len(step_1) != 3:
        raise ValueError('Entry must be three digits')
    if abs(int(step_1[0]) - int(step_1[2])) < 2:
        raise ValueError('First and last must digits must be more than 2 apart')
    step_2 = input("Enter the reverse of the first number, obtained "
                   "by reading it backwards: ")
    if not (step_2[2] == step_1[0]
        and step_2[1] == step_1[1]
        and step_2[0] == step_1[2]):
        raise ValueError('The second number must be the reverse of the first')
    step_3 = input("Enter the positive difference of these numbers: ")
    if int(step_3) != abs(int(step_2) - int(step_1)):
        raise ValueError('The third number is not the pos diff of the last two')
    step_4 = input("Enter the reverse of the previous result: ")
    if not (step_4[2] == step_3[0]
        and step_4[1] == step_3[1]
        and step_4[0] == step_3[2]):
        raise ValueError('The fourth number must be the reverse of the third')
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

arithmagic()

#Problem 2

from random import choice

def random_walk(max_iters=1e12):
    try:
        walk = 0
        directions = [1, -1]
        for i in range(int(max_iters)):
            walk += choice(directions)
    
    except KeyboardInterrupt:
        print('Process interrupted at iteration', i)
    
    finally:
        return walk

#Problem 3
class ContentFilter():
    def __init__(self, filename):
       self.filename = filename

    file_exists = False
    while file_exists == False:
        try:
            with open(filename, 'r') as file_chosen:
                file_exists = True
                self.filename = filename
                self.content = file_chosen.read()
        except:
            filename = input('Please enter a valid file name')

   
    
        
      











