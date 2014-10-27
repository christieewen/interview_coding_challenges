# http://en.wikipedia.org/wiki/Fibonacci_number
# Given n, return an array of a fibonacci sequence of length n.
# In modern usage, 0 is the first number.

def ret_fibonacci(n):

    fibonacci = []
    if n < 1:
        return fibonacci
    fibonacci.append(0)
    index = 1
    num = 1
    temp = 1
    numLast = 0

    while index < n:
        fibonacci.append(num)
        temp = num + numLast
        numLast = num
        num = temp
        index = index + 1

    return fibonacci

# Test it out
print ret_fibonacci(5)
print ret_fibonacci(0)
print ret_fibonacci(1)
print ret_fibonacci(30)
