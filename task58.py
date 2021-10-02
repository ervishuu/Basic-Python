# a python program to find the length of a string without using len() function

str = input("Enter a string: ")

for i in range(len(str)):
    print(str[i],end="")

print("\nlength of string is ",i+1)