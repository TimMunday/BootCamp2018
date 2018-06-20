# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:23:38 2018

@author: Tim
"""
import pytest
import operate_mod as om

def test_operate():
    assert om.operate(3, 2, '+') == 5, 'Fails on plus'
    assert om.operate(3, 2, '-') == 1, 'Fails on minus'
    assert om.operate(3, 2, '*') == 6, 'Fails on multiply'
    assert om.operate(3, 2, '/') == 1.5, 'Fails on divide'
    with pytest.raises(TypeError) as excinfo:
        om.operate(3, 2, 3)
    assert excinfo.value.args[0] == "oper must be a string"
    with pytest.raises(ZeroDivisionError) as excinfo:
        om.operate(3, 0,'/')
    assert excinfo.value.args[0] == "division by zero is undefined"
    with pytest.raises(ValueError) as excinfo:
        om.operate(3, 2,'b')
    assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"