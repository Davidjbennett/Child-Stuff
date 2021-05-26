'''
Project:P5 trees
Author: David Bennett
Course: cs 2420
Date: 4/5/2021

Description: A paragraph from around the world in 80 days is taken
and the letters are organized into a tree as a key value pair, where
the key is the letter and the value is the number of times the letter
shows up in the tree

Lessons Learned:
-The remove function is very confusing.
-Learned new things from each function and how to set up a tree
-Learned how to better intergrate code

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree.
    
    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''
    my_tree = BST()
    with open("D:\\UVU\\DavidBennett\\CS2420\\Mod5\\P5\\around-the-world-in-80-days-3.txt", "r") as f:
        paragraph = f.read()
        for letter in paragraph:
            if letter.isalnum():
                try:
                    letter_obj = my_tree.find(Pair(letter))
                    letter_obj.count += 1
                except ValueError:
                    my_tree.add(Pair(letter))
    # print(my_tree.inorder())
    return my_tree
    # print(my_tree)
    # print(my_tree.inorder())
    # print(my_tree.find(Pair('a')))
    # print(my_tree.find(Pair('A')))
    # print(my_tree.inorder())

def main():
    ''' Program kicks off here.

    '''
    make_tree()
    
        
    
if __name__ == "__main__":
    main()
