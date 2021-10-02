# A python program to know how to define aa function inside another function

def myfunc(str):
    def message():
        return "hello "
    return message()+str

print(myfunc("vishvanath"))