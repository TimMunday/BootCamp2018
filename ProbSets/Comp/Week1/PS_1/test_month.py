# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:55:57 2018

@author: Tim
"""

import month

def test_month():
    assert month.month_length('September') == 30, 'month length fails'
    assert month.month_length('January') == 31
    assert month.month_length('February', leap_year=True) == 29
    assert month.month_length('February', leap_year=False) == 28
    assert month.month_length('check') == None