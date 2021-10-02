# a python program to know how a function can return another function

def display():
    def message():
        return "how are you...."

    return message()

print(display())