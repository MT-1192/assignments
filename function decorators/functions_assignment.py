#1.Write a Python function to find the maximum of three numbers.
'''def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list)   
x = int(input("Enter First number: "))
y = int(input("Enter Second number: "))
z = int(input("Enter Third number: "))
print("Maximum Number is: ",maximum(x, y, z))'''

'''def maximum(a,b,c):
   if (a>=b) and (a>=c):
    largest = a
   elif (b>=a) and (b>=c):
    largest = b
   else:
    largest = c
   return largest
a = 17
b = 20
c = 32
print(maximum(a,b,c))'''

'''a = 17
b = 20
c = 32
print(max(a,b,c))'''

#2.Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
'''def sum(num):
    total = 0
    for i in num:
        total += i
    return total
print(sum((8,2,3,0,7)))'''

#3.Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
'''def multiply(num):  
    total = 1
    for i in num:
        total *= i  
    return total  
print(multiply((8, 2, 3, -1, 7)))'''

#4.Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
'''def fun(x):
  return x[::-1]
given_string = fun("1234abcd")
print(given_string)'''

#5.Write a Python function to calculate the factorial of a number. The function accepts the number as an argument.
'''def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("enter the number: "))
print(factorial(n))'''

#6.Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
'''given_string="The quick Brow Fox"
def char(given_string):
  upper = 0
  lower = 0
  for i in given_string:
      if i>='a' and i<='z':
       lower += 1

      if i >='A' and i<='Z':
       upper += 1
  print("No. of upper case characters are",upper)
  print("No. of lower case characters are",lower)
char(given_string)'''

#7.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
'''def unique_list(l):
  x = []
  for i in l:
    if i not in x:
      x.append(i)
  return x
print(unique_list([1,2,3,3,3,3,4,5]))'''

#8.Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]
'''def is_even_num(l):
    even_num = []
    for n in l:
        if n % 2 == 0:
            even_num.append(n)
    return even_num
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))'''

#9.Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow
'''n=input("enter the string: ") 
l=n.split('-') 
l.sort() 
print('-'.join(l))'''

#10.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30
'''def squared_numbers():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l)
squared_numbers()'''

#11.Write a Python program to create any chain of function decorators.
#12. Write a Python program to access a function inside a function.
'''def f():
    def inner(a,b):
        print("sum:",a+b)
    inner(10,20)
f()'''


     
      