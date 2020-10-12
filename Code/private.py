'''
    private.py

    Illustrates obfuscation of class attributes.
'''

class PrivateData:
    def __init__(self,attr1,attr2):
        self.__attr1 = attr1    # Inside the class we use "__attr1"
        self.__attr2 = attr2    # Inside the class we use "__attr2"

p = PrivateData(1,'two')
print(vars(p))

try:
    print(p.attr1)
except:
    print("No such attribute attr1")

print(p._PrivateData__attr1)    # Outside the class must use the mangled name

''' Output:
{'_PrivateData__attr1': 1, '_PrivateData__attr2': 'two'}
No such attribute attr1
1
'''
