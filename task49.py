# python program to know wether a sub string exits in main strings or not

str1 = input("Enter the main string: ")
str2 = input("Enter the substring : ")
if str2 in str1:
    print("sub string {} found in main string {}".format(str2,str1))
else:
    print("sub string {} not found in main string {}".format(str2,str1))