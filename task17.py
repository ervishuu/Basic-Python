# craete list retrive only negative number from the list
data = []

num = int(input("Enter how many element do you want to store: "))
for i in range(num):
    in_data = int(input("Enter the element: "))
    data.append(in_data)
# retive the negative element from data list
for element in data:
    if element > 0:
        pass
    else:
        print(element)
