# a python program to display a group of string

def string(lst):
    """to display the string"""
    for i in lst:
        print(i)
data = [x for x in input("Enter the string: ").split(",")]
string(data)