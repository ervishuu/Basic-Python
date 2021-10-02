#a function to accept a group of number and find their total average

def calculation(lst):
    """find the total length of list"""
    length = len(lst)
    sum = 0
    for i in lst:
        sum+=i
    avg = sum/length
    print("total sum is: ",sum)
    print("total avrage is : ",avg)

data = [int(x) for x in input("Enter the list (give space) :").split(" ")]
calculation(data)
