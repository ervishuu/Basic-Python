# a python program to create a list with employee data and then retrieve a particular employee details

emp = []
num = int(input("Enter how many employee: "))
for i in range(num):
    print("Enter details of {} employee".format(i+1))
    roll_ID=int(input("enter roll Id : "))
    emp.append(roll_ID)
    name = input("Enter the employee name: ")
    emp.append(name)
    salary = float(input("Enter the salary: "))
    emp.append(salary)

print("list is created ")
id = int(input("Enter the roll ID: "))

for i in range(len(emp)):
    if id == emp[i]:
        print("ID: ",emp[i])
        print("Name: ",emp[i+1])
        print("Salaray: ",emp[i+2])
        break
