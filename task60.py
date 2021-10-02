# a python program to calculate factorial values of numbers
def fact(n):
    prod = 1
    while n >=1:
        prod = prod*n
        n = n-1
    return prod

for i in range(1 , 11):
    print("Factorial of {} is {}".format(i,fact(i)))