# A python program to understand how a function returns two values

def sum_sub(a,b):
    c = a+b
    d = a-b
    return c,d


sum ,sub = sum_sub(5,10)
print(sum,sub)