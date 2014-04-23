###################################

def ret_fibonacci(ith):
    fibonacci = []
    fibonacci.append(0)
    index = 1
    num = 1
    temp = 1
    numLast = 0	
    
    print fibonacci[0]
    while index <= ith:
        print num
        fibonacci.append(num)
        temp = num + numLast
        numLast = num
        num = temp
        index = index + 1

    return fibonacci[ith]
        
print ret_fibonacci(29)
