# python program to generate fabinocci series

in_data = int(input("How many fabonacci's: "))

f1 =0
f2 =1
temp =2
if in_data == 0:
    print("0")
elif in_data == 1:
    print("1")
else:
    print(f1)
    print(f2)
    while temp < in_data:
        f3 = f1+f2
        print(f3)
        f1,f2 = f2,f3
        temp+=1

