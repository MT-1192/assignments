a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
largest_number = 0
if a > b and a > c:
    largest_number = a 
if b > a and b > c:
    largest_number = b

if c > a and c > b:
    largest_number = c 

print(largest_number, "is the largest of three number")
