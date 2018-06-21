# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 14:29:19 2018

@author: Tim
"""
from object_oriented import ComplexNumber 

def test_ComplexNumber():
    a=3
    b=4
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)
    
    #Validate the constructor
    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real and self.imag incorrectly")
        
    #Validate conjugate() by checking the new number's imag attribute
    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print('conjugate() failed for', py_cnum)
    
    #Validate __str__()
    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)
    
    #Validate __abs__()
    if abs(py_cnum) != abs(my_cnum):
        print('absolute value failed for', py_cnum)
    
    #Validate __eq__()
    if py_cnum != my_cnum:
        print('equality failed')
    
    #Validate __add__()
    if py_cnum + py_cnum.conjugate() != my_cnum + my_cnum.conjugate():
        print('Addition failed')
    
    #Validate __sub__()
    if py_cnum - py_cnum.conjugate() != my_cnum - my_cnum.conjugate():
        print('Substituion failed')
        print(py_cnum - py_cnum.conjugate())
        print(my_cnum - my_cnum.conjugate())
        
    #Validate__mul__()
    if py_cnum*py_cnum.conjugate() != my_cnum*my_cnum.conjugate():
        print('Mult failed')
        
    #Validate__truediv__()
    if py_cnum/py_cnum.conjugate() != my_cnum/my_cnum.conjugate():
        print('Div failed')

    print('test ended')

test_ComplexNumber()
