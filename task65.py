# a python program to access global variable inside a function and modify it

a =1 #this is global varible

def myfunction():
    global a
    print("original value of global variable is : ",a)
    a =5
    print("after modify global variable is : ",a)

myfunction()
print("value of a : ",a)
