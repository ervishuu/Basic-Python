# python program to find the first occurrence of sub string in a given string using index method

str1 = input("Enter the main string: ")
str2 = input("Enter the substring: ")

try:
    pos = str1.index(str2, 0, len(str1))
    print("Substring {} found at location {} ".format(str2,pos))

except ValueError as vr:
    print("not found ")