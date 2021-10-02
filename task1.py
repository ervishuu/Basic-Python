# a python program to display a group of message when condition is true

num = int(input("Enter the number in between 1 to 30: "))
if num >= 1 and num <=10:
    print(" 1 to 10 number")
elif num >11 and num <=20:
    print("11 to 20")
elif num >21 and num <=30:
    print("21 to 30")
else:
    print("please enter valid data")