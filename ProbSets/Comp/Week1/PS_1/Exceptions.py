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
    if type(step_1) != int:
        raise ValueError('Entry must be an integer')
    step_2 = input("Enter the reverse of the first number, obtained "
                   "by reading it backwards: ")
    step_3 = input("Enter the positive difference of these numbers: ")
    step_4 = input("Enter the reverse of the previous result: ")
    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")

arithmagic()
