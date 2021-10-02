# a python to sort the list element using bubble sort technique
#crate empty list
x = []
num = int(input("Enter the lenght of list: "))
for i in range(num):
    data = int(input("Enter the element: "))
    x.append(data)

print("Origianl list : ",x)

#bubble sort
flage = False
for i in range(num-1):
    for j in range(num-1-i):
        if x[j]>x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            flage = True

    if flage==False:
        break
    else:
        flage = False

print("Sorted list: ",x)
