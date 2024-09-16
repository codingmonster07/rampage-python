




def fib(n):
 
    # base case 
    # if number is 1 and 0 return 1 and 0
    if n == 1 or n == 0:
        return n
 
    # least amount of work to perform in each recursive call
    return fib(n - 1) + fib(n - 2)
 
result = fib(4)
print(result)