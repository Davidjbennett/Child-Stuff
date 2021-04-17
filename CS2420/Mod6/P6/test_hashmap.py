'''
Project: Recomputation versus Caching
Author: George Rudolph
Course:  CS 2420 Fall 2020
Date: 3 Nov 2020

Description: 8 basic test cases to automate grading of a student's hashtable
implementation.
Each HashMap ADT required operation is tested at least once.

To run:
Assume you have pytest module installed.
Assume you have the student's hashmap.py to run.

Open a terminal window in that directory, type 'python -m pytest' as the command and press
enter.
'''

import pytest
from hashmap import HashMap

def test_empty_map():
    hm = HashMap()
    assert hm.capacity() == 7
    assert hm.size() == 0

def test_remove():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    hm.remove((3,3))
    print(hm)
    with pytest.raises(KeyError):
        hm.get((3,3))
    assert hm.get((5,5)) == 6

def test_clear():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    hm.clear()
    assert hm.capacity() == 7
    assert hm.size() == 0

def test_keys():
    hm = HashMap()
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    keys2 = hm.keys()
    keys2.sort()
    assert keys == keys2
    
def test_get_set():
    hm = HashMap()
    with pytest.raises(KeyError):
        hm.get((0,0))
    
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    for k,v in zip(keys,values):
        hm.set(k,v)
    assert hm.get((5,5)) == 6
    assert hm.get((9,9)) == 10
    hm.set((2,2), 409)
    assert hm.get((2,2)) == 409

def test_rehashing():
    keys = [(r,r) for r in (range(10))]
    values = list(range(1, 11))
    hm = HashMap()
    for k,v in zip(keys,values):
        hm.set(k,v)
    assert hm.size() == 10
    assert hm.capacity() == 13
        
def test_code_quality():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('hashmap.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected
