# a python program to handle the Assertion Error exceptation that given by assert statement

x = int(input("Enter the number greater then 0: "))
try:
    assert x > 0
    print("you entered ",x)

except AssertionError :
    print("Wrong input.....")
