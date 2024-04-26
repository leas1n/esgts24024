# my_code.py
 
def factorial_recursive(n):
    if(n<0):
        return "Factorial is not defined for negative numbers."
 
    if (n==0):
        return 1
    else:
        return n * factorial_recursive(n-1)
    # if-else
# def factorial_recursive
 
def factorial_iterative(n):
    if(n<0):
        return "Factorial is not defined for negative numbers."
 
    if (n==0):
        return 1
    else:
        mult = 1
        # range(1, n+1) is the interval [1,n]
        for factor in range(1, n+1):
            mult*=factor
        # for
        return mult
    # if-else
