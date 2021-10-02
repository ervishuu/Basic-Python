# a python program to sort a group of string into alphabetical order

str = []
num = int(input("Enter how many string do you want: "))

for i in range(num):
    data= input("Enter {} string :" .format(i+1))
    str.append(data)

#sort array
str1 = sorted(str)
print(str)
print(str1)