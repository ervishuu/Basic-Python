# a python program to know how to pass a function as parameter to another function

def display(myfun):
    return "hello "+myfun

def message():
    return "vishvanath"

print(display(message()))