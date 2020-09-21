def myRange(p, q = None, r = None):

    if p == 0 and q == None and r == None:
        return []
  
    if r == None:
        step = 1
    else:
        step = r

    if q == None:
        start = 0
        stop = p
    else:
        start = p
        stop = q

    res = []
    i = start

    while True:
        res.append(i)

        if step > 0 and i + step >= stop:
                break          
        elif step < 0 and i + step <= stop:
                break
        else:
            i = i + step           

    return res


print('myRange(0):',myRange(0))
print('myRange(1):',myRange(1))
print('myRange(10):',myRange(10))
print('myRange(3, 9):',myRange(3, 9))
print('myRange(2, 10, 2):',myRange(2, 10, 2))
print('myRange(10, 2, -2):',myRange(10, 2, -2))