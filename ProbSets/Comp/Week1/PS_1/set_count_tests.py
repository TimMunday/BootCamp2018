# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:15:22 2018

@author: Tim
"""

import numpy as np
import itertools as it

def count_sets(cards):
    """Return the number of sets in the provided Set hand.
    Parameters:
        cards (list(str)) a list of twelve cards as 4-bit integers in
        base 3 as strings, such as ["1022", "1122", ..., "1020"].
    Returns:
        (int) The number of sets in the hand.
    Raises:
        ValueError: if the list does not contain a valid Set hand, meaning
            - there are not exactly 12 cards,
            - the cards are not all unique,
            - one or more cards does not have exactly 4 digits, or
            - one or more cards has a character other than 0, 1, or 2."""
    combs=list(it.combinations(cards, 3))
    numb_sets=np.zeros(len(combs))
    for i, val in enumerate(combs):
        if is_set(*val):
            numb_sets[i]=1
    
    if len(cards)!=12:
        raise ValueError('There are not exactly twelve cards')
        
    if len(cards)!=len(set(cards)):
        raise ValueError('The cards are not all unique')
    
    for i in cards:
        if len(i) != 4:
            raise ValueError('One or more cards does not have exactly 4 digits')
        for j in i:
            if j!=0 or j!=1 or j!=2:
                raise ValueError('One or more cards has a character other than 0, 1 or 2')
    
    print(sum(numb_sets))
    return sum(numb_sets)

hand1 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1020"]
count_sets(hand1)

import card_game as cg

def test_count_sets():
    assert cg.count_sets(hand1) == 6
    with pytest.raises(ValueError) as excinfo:
        cg.count_sets(hand1.append(['2000']))
        cg.count_sets(["1122", "1122", "0100", "2021",
                       "0010", "2201", "2111", "0020",
                       "1102", "0210", "2110", "1020"])
        cg.count_sets(["11222", "1122", "0100", "2021",
                       "0010", "2201", "2111", "0020",
                       "1102", "0210", "2110", "1020"])
        cg.count_sets(["1142", "1122", "0100", "2021",
                       "0010", "2201", "2111", "0020",
                       "1102", "0210", "2110", "1020"])

def is_set(a, b, c):
    """Determine if the cards a, b, and c constitute a set.
    Parameters:
        a, b, c (str): string representations of 4-bit integers in base 3.
            For example, "1022", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, b,
            and c are either the same or all different for i=1,2,3,4.
        False if a, b, and c do not form a set."""
    test_vec=np.zeros(4)
    for i in range(0, 4):
        if a[i]==b[i]==c[i]:
            test_vec[i]=1
        if a[i]!=b[i] and b[i]!=c[i] and a[i]!=c[i]:
            test_vec[i]=1
    if sum(test_vec)==4:
        return True
    else:
        return False

def test_is_set():
    assert cg.is_set(['1022', '1122', '1020']) == False
    assert cg.is_set(['1022', '1122', '1222']) == True
    

