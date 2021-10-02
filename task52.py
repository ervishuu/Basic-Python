# a python program to display all position of substring in a given main string

str1 = input("Enter the main string: ")
str2 = input("Enter the substring: ")

i = 0
flag = False
while i <= len(str1):
    pos = str1.find(str2,i,len(str1))
    if pos != -1:
        print("sub string {} found at location {}".format(str2,pos+1))
        i = 1 + pos
        flag= True
    else:
        i+=1

if flag == False:
    print("Substring not found")
