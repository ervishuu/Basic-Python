# a python program to get a copy of global varible into a function and work with it

a =1 # this is global varible
def myfunction():
    a = 5
    x= globals()["a"]  # copy global value into x
    print("global value of a : ",x)
    print("local value of a : ",a)

myfunction()
print("value of a : ",a)