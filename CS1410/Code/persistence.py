''' persistence.py:

    Illustrates the pickle module.
    Run in pythontutor.com to visualize process.
'''

import pickle

# Create some data structures
mylist = [1,2,3]
mytup = (4,5,6)
mytext = "ten"
myhash = {'alist':mylist, 'atuple':mytup, 'astring':mytext}

# Persist them to a file
with open('keep.dat','wb') as f:
    pickle.dump(mylist,f)
    pickle.dump(mytup,f)
    pickle.dump(mytext,f)
    pickle.dump(myhash,f)
print([item for item in vars() if item[0] != '_'])

# Delete all objects
del mylist; del mytup; del mytext; del myhash; del f
print([item for item in vars() if item[0] != '_'])

# Reconstitute the objects
with open('keep.dat','rb') as f:
    mylist = pickle.load(f)
    mytup = pickle.load(f)
    mytext = pickle.load(f)
    myhash = pickle.load(f)
print([item for item in vars() if item[0] != '_'])

''' Output:
['pickle', 'mylist', 'mytup', 'mytext', 'myhash', 'f']
['pickle']
['pickle', 'f', 'mylist', 'mytup', 'mytext', 'myhash']
'''