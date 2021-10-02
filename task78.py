# A python program to find a commom element in two list

data1 = ["vishu","shubham","akash","saurabh","shri"]
data2 = ["Vishu","sanket","saurabh","akash","nilesh","pravin"]

print(data1)
print(data2)
new_data1= set(data1)
new_data2= set(data2)

common_data= new_data1.intersection(new_data2)
print("common element are: ",common_data)