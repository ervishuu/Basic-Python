# a python program to search for the position of a string in a given group of string
str = []

num = int(input("How many strings do you want : "))
for i in range(num):
    str.append(input("Enter the {} string: ".format(i)))

element = input("Enter the string which we want to search : ")

flage = False

for i in range(len(str)):
    if element ==str[i]:
        print("string {} found at location {}".format(element,i+1))
        flage = True
if flage ==False:
    print("String is not found")