# Search element in the list

data =[44,66,77,43,35,8787,55]

num = int(input("Enter the number which we want to search: "))
for element in data:
    if element == num:
        print("The number {} is found".format(num))
        break
else:
    print("element is not found.......")
