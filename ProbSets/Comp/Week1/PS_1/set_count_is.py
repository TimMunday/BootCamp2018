# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 20:15:22 2018

@author: Tim
"""

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
            - one or more cards has a character other than 0, 1, or 2.
"""
pass

import card_game as cg

hand1 = ["1022", "1122", "0100", "2021",
         "0010", "2201", "2111", "0020",
         "1102", "0210", "2110", "1020"]

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
        False if a, b, and c do not form a set.
"""
pass

def test_is_set():
    

