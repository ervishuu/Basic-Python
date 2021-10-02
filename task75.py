#a python program to find maximun minimum element in a list of element
x =[]
num = int(input("Enter the length of list: "))
for i in range(num):
    m = int(input("Enter the element: "))
    x.append(m)

print(x)
print("Maximun element in list",max(x))
print("Minimum element in list",min(x))