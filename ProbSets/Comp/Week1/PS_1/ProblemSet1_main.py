# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 07:44:12 2018

@author: Tim
"""
# Lab 4

# Problem 1:

import numpy as np

def p1(X, Y):
    ''' blah blah
    '''
    answer=np.dot(X, Y)
    return answer

A = np.array([[3, -1, 4],[1, 5, -9]])
B = np.array([[2, 6, -5, 3],[5, -8, 9, 7],[9, -3, -2, -3]])

p1_answer = p1(A, B)
print(p1_answer)

#Problem 2:

def p2(X):
    int_1=np.dot(X, X)
    int_2=np.dot(X, int_1)
    int_3=9*np.dot(X, X)
    int_4=15*X
    output_2 = int_3 - int_2 - int_4
    return output_2

A_2 = np.array([[3,1,4],[1,5,9],[-5,3,1]])
p2_answer = p2(A_2)
print(p2_answer)

#Problem 3:

def p3():
    A_3_int=np.ones((7,7))
    A_3=np.triu(A_3_int)
    B_3_int_1=np.transpose(np.triu(-np.ones((7,7))))
    B_3_int_2=np.triu(5*np.ones((7,7)), 1)
    B_3=B_3_int_1 + B_3_int_2
    output_3_int = np.dot(A_3, B_3)
    output_3 = np.dot(output_3_int, A_3)
    print(output_3)
    return output_3
    
p3()

#Problem 4:

def p4(X):
    Y=X
    mask = Y<0
    Y[mask] = 0
    print(Y)
    return Y

#Problem 5:
    
def p5():
    A_4=np.array([[0,2,4],[1,3,5]])
    B_4=np.tril(3*np.ones((3,3)))
    C_4=-2*np.eye(3)
    LHS=np.vstack((np.zeros((3,3)), A_4, B_4))
    MHS=np.vstack((np.transpose(A_4), np.zeros((2,2)), np.zeros((3,2))))
    RHS=np.vstack((np.eye(3), np.zeros((2,3)), C_4))
    output_5=np.hstack((LHS, MHS, RHS))
    print(output_5)
    return

p5()

#Problem 6:

def p6(X):
    A_6=X.sum(axis=1)
    Y=X/A_6[:, np.newaxis]
    print(Y)
    return Y

#Problem 7:

def p7():
    grid=np.load('C:/Users/Tim/Documents/OSM/Mybootcampcopy/BootCamp2018/Computation/Wk1_PyIntro/grid.npy')
    hmax= np.max(grid[:,:-3] * grid[:,1:-2] * grid[:,2:-1] * grid[:,3:])
    vmax= np.max(grid[:-3,:] * grid[1:-2, :] * grid[2:-1, :] * grid[3:,:])
    drmax= np.max(grid[:-3, :-3]*grid[1:-2, 1:-2]*grid[2:-1, 2:-1]*grid[3:, 3:])
    lrmax= np.max(grid[3:, :-3]*grid[2:-1, 1:-2]*grid[1:-2, 2:-1]*grid[:-3, 3:])
    print(hmax)
    print(vmax)
    print(drmax)
    print(lrmax)
    return
p7()

#Lab 2 - Standard Library

#Problem 1:

def p8(X):
    print(min(X), max(X), sum(X)/len(X))
    return
p8()

#Problem 2:

#int
int_1 = int(5)
int_2 = int_1
int_2 = 6

#str
str_1 = 'hello'
str_2 = str_1
str_2 = 'helli'

#list
list_1 = [1, 'a', 2, 'b']
list_2 = list_1
list_2[3] = 3

#tuple
tup_1 = (1, 'two', float(3.1))
tup_2 = tup_1
tup_2 += (1,)

#set
set_1 = {'a', 'b', 'c'}
set_2 = set_1
set_2.add('d')

print(int_1 == int_2, str_1 == str_2, list_1 == list_2, tup_1 == tup_2, set_2 == set_1)

#Problem 3:

import math
import calculator as cac

def p9(X, Y):
    hypotenuse = math.sqrt(cac.mysum(cac.myproduct(X, X), cac.myproduct(Y,Y)))
    print(hypotenuse)
    return hypotenuse

#Problem 4:

from itertools import chain, combinations
def p10(X):
    Y = list(X)
    return chain.from_iterable(combinations(Y, r) for r in range(len(Y)+1))

output_10 = list(p10(['a', 'b', 'c']))
print(output_10)

#Problem 5:

#In set_count_tests script file

#Lab 7

#Problem 1:
# Test is called test_smalfac.py
# Test fails because by taking the integer of the square root of n, we lose some solutions (for 4,6,8)

#New improved function

def my_smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    for i in range(2, int(n**.5)+1):
        if n % i == 0: return i
    return n

#Problem 2:
    #In test script files
    
#Problem 3:
    #In test script files

#Problem 4:
    #In test script files


