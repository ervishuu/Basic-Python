# A Python program to storing student marks into an array and finding total marks and percentages of marks.
from array import *
data =input("Enter the marks: ").split(",")

#store the marks in array
marks = [int(num) for num in data]

print("Marks:",marks)
sum = 0
for i in marks:
    sum+=i

print("Total Sum: ",sum)
lenght = len(marks)

percentage = sum/lenght

print("Percentage: ",percentage)