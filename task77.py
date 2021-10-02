# a python program to know many time an element occurred in the list

x = []
num=  int(input("Enter the lenght of element: "))

for i in range(num):
    data = int(input("Enter the element: "))
    x.append(data)

print("List: ",x)
element = int(input("Enter the elemet to count: "))

count = 0
for i in range(num):
    if element == x[i]:
        count+=1

print("count of {} is {}".format(element,count))