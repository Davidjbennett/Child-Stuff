#den will default to 1 if its not input
def frac2dec(num, den=1):
    return num/den

#!recursive function
def countdown(number):
    print(number, end='...')

    #!base case
    if number <= 0:
        return

    #!recursive case
    countdown(number - 1) #!has a changing parameter

#the reason we want to use a recursive function is some problems 
# are more easily solved with recursion. For ex. if you want to
# read a whole directory its almost impossible to do with while
#loops, whereas recursion takes a few lines of code. or factorials
def display_range(lower, higher):
    #!base case
    if lower > higher:
        return
    
    print(lower, end = ' ')

    #!recursive case
    display_range(lower+1, higher)

def summation(lower, upper):
    """returns the sum of the numbers from lower through upper"""
    #!base case
    if lower > upper:
        return 0

    #!recursive case
    return lower + summation(lower + 1, upper)

def factorial(number):
    if number == 1: #!base case
        return number
    return number * factorial(number - 1) #! recursive case

count = 0

def old_fib(n):
    if n < 3:
        return n
    return old_fib(n-1) + old_fib(n-2)

cache = {}

def fib(n):
    global count
    count += 1
    if n in (0,1):
        result = n
    elif n in cache:
        result = cache[n]
    else:
        result = fib(n-1) + fib(n-2)
        cache[n] = result
    return result

def fib_loop(n):
    if n in (0,1):
        return n
    first,second = 1,1
    for n in range(2,n):
        first,second = second,first+second
    return second


if __name__ == "__main__":
    # print(frac2dec(10,2))
    # print(frac2dec(10))
    print(countdown(10))
    print()
    print(display_range(0,10))
    print(summation(1,5))
    #!how to add commas every 3 numbers
    print('{:,}'.format(factorial(13)))
    print(old_fib(20))
    print(fib(50))
    print(count)
    print('{:,}'.format(fib_loop(10)))

#can end a line with space so it doenst do newline
#!plain for loop
#    for i in range(10):
#        print(i, end=' ')