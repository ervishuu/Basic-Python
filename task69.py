# A python program to calculate factorial values using recursion
def factorial(n):
    """to find factorial of n"""
    if n ==0:
        result = 1
    else:
        result = n*factorial(n-1)
    return result

for i in range(1,11):
    print("factorial of {} is {}".format(i,factorial(i)))
