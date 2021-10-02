# a python program to know the type of character entered by the user

str = input("Enter the string: ")
num = str[0]
if num.isalnum():
    if num.isalpha():
        if num.isupper():
            print("it is a capital letter")
        else:
            print("it is lower case letter")
    else:
        print("it is a number")
elif num.isspace():
    print("It is a space")
else:
    print("it may be a special character")