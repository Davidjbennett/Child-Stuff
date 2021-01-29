def filter_list(l):
    answer = [char for char in l if type(char) == int]
    return answer

def filter_list1(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

def filter_list2(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

def filter_list3(l):
  'return a new list with the strings filtered out'
  return [e for e in l if isinstance(e, int)]

def filter_list4(l):
    return filter(lambda x: not type(x) is str, l)

print(filter_list([1,2,'a','b']),[1,2])
print((filter_list([1,'a','b',0,15]),[1,0,15]))
print((filter_list([1,2,'aasf','1','123',123]),[1,2,123]))