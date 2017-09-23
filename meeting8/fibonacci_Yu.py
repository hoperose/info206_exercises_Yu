#define a function to compute the nth Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#it is not efficient way to use the recursive algorithm to compute the nth
#Fibonacci number since the fib() function gets called with the same values
#duplicates an enormous amount of work. Instead, use an iterative function
#is a more useful way in computing the nth Fibonacci number
