'''
Project: pytest BST for Phileas Fogg Project
Author: George Rudolph
Course:  CS 2420 Fall 2020
Date: 1 Nov 2020

Description: 11 test cases to automate grading of a student's BST implementation.
Each BST ADT required operation is tested at least once.
You'll notice that add() and find() are not tested explicitly, except find()
on an empty tree. That's because these functions have to work
in order to build a correct tree at all--if they don't, other tests will fail.

Thinking of dependencies, consider that a test file like this takes
the place of main(), or some other code that exercises the implementation,
so it willl likely have similar dependencies.

Notes:
1. This test depends on the input file "around-the-world-in-80-days-3.txt"
2. This test file is given to students to use for developing their BST code.
3. This is not intended to be exhaustive unit testing, just enough to show
   that their implementation is a good enough implementation of the ADT.
4. These tests ARE intended to automate grading.
5. This version assumes an OOP implementation of the BST.
   A Procedural or Functional version would be slightly different,
   mainly the first parameter would be the tree being operated on.

To run:
Assume you have pytest module installed.
Assume you have the student's bst.py, student's copy of test_bst.py and
input file all in same directory.

Open a terminal window in that directory, type 'pytest' as the command and press
enter.
'''
import pytest
from random import seed, sample
from bst import BST
from main import Pair, make_tree

def test_create_BST():
    bst = BST()
    assert bst.size() == 0
    assert bst.is_empty()

def test_tree_size():
    bst = make_tree()
    assert bst.size() == 57

def test_tree_height():
    bst = make_tree()
    assert bst.height() == 11
    
def test_find_empty():
    with pytest.raises(ValueError):
        bst = BST()
        item = bst.find(Pair('A'))

def test_remove_root():
    bst = make_tree()
    bst.remove(Pair('C'))
    pre = bst.preorder()
    assert pre[0] == Pair('D')

def test_remove_internal():
    bst = make_tree()
    pre = bst.preorder()
    i = pre.index(Pair('g'))
    bst.remove(Pair('g'))
    pre = bst.preorder()
    assert pre[i] == Pair('f')

def test_remove_leaf():
    bst = make_tree()
    bst.remove(Pair('z'))
    pre = bst.preorder()
    assert pre[-1] == Pair('w')
    
def test_preorder():
    bst = make_tree()
    assert bst.preorder()[27] == Pair('R',20)
    
def test_inorder():
    bst = make_tree()
    assert bst.inorder()[27] == Pair('T',34)
    
def test_postorder():
    bst = make_tree()
    assert bst.postorder()[27] == Pair('W',13)

def test_rebalance():
    bst = make_tree()
    original_height = bst.height()
    tree_data = bst.rebalance()
    assert not original_height == bst.height()
    
def test_code_style():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('bst.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected
