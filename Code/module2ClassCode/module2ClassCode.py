
def frac2dec(num, den=1):
    return num/den


def count_down(number):
    print(number, end='... ')
    
    #base case
    if number <= 0:
        return
    
    #recursive case
    count_down(number - 1) #diminishing parameter (changing parameter)

def display_range(lower, higher):
    #base case
    if lower > higher:
        return

    print(lower, end=' ')

    #recursive case
    display_range(lower + 1, higher)

def summation(lower, upper):
    """Returns the sum of the numbers from lower through upper"""
    #base case
    if lower > upper:
        return 0
    
    #recursive case
    return lower + summation(lower + 1, upper)

def factorial(number):
    #base case
    if number == 1:
        return number
    
    #recursive case
    return number * factorial(number - 1) #diminishing!

count = 0

def oldFib(n):
    global count
    count += 1
    if n in (0, 1):
        return n
    return oldFib(n-1) + oldFib(n-2)

cache = {}

def fib(n):
    global count
    count += 1

    if n in (0, 1):
        result = n
    elif n in cache:
        result = cache[n]
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
    return result

if __name__ == "__main__":
    #print(frac2dec(10, 2))
    #print(frac2dec(7))

    #for i in range(10):
    #    print(i, end=' ')
    count_down(3)
    print()
    display_range(0, 10)
    print()
    print(summation(1, 5))
    print(factorial(5))

    print("fib of 50 is", fib(10))
    print("number of function calls:", count)
    count = 0
    print("old fib", (oldFib(10)))
    print("number of function calls:", count)