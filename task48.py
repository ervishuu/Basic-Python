# a python progarm to access each element of a string in forward and reverse order using while loop
str = "I love python"

i = 0
print("Original string\n")
while i < len(str):
    print(str[i],end=" ")
    i+=1
i = 1
print("\nReverse string\n")
while i <= len(str):
    print(str[-i],end=" ")
    i+=1