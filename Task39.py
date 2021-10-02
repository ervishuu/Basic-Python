# a python program to create an array using logspace()

from numpy import *

a = logspace(1,20,5)
b = linspace(1,20,5)

print(a)
print(b)

print(type(a))
print(type(b))