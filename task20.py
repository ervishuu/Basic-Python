#write a program to display prime number
in_data = int(input("Up to what number: "))

for i in range(2,in_data+1):
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        print(i)