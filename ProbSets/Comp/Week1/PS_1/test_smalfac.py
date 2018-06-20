# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 15:11:57 2018

@author: Tim
"""

import smalfac

def test_smalfac():
    assert smalfac.smallest_factor(1) == 1, 'smallest factor fails'
    assert smalfac.smallest_factor(10) == 2, 'smallest factor fails'
    assert smalfac.smallest_factor(6) == 2, 'smallest factor fails'
    