# A python program to find the first occurrence of sub string in a given main string

str1 = input("Enter the main string: ")
str2 = input("Enter the sub string: ")

pos = str1.find(str2,0,len(str1))
if pos == -1:
    print("substring not found")
else:
    print("{} substring found at location {} in main string {}".format(str2,pos+1,str1))