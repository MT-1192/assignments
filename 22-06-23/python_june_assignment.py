#1.Calculate the sum of all numbers from 1 to a given number.
'''number = int(input("enter the number: "))
sum = 0
for i in range(1,number+1):
    sum = sum + i
print(sum)'''

#2.Write a program to print multiplication table of a given number.
'''n = int(input("enter the number: "))
for i in range(1, 11):
    print(str(n) + " x " + str(i) + " = " + str(i*n))'''

#3.Display numbers from a list using loop.
'''a = [1,2,3,4,5]
for i in range(len(a)):
    print(a[i])'''

#4.Count the total number of digits in a number.
'''n = int(input("enter the number: "))
count=0
for i in str(n):
    count=count+1
print("The no.of digits in a number are: ",count)'''

#5.Print list in reverse order using a loop.
'''n = int(input("enter the number: "))
list_a = []
for i in range(n):
    num = input()
    list_a += [num] 
for i in range(n):
    print(list_a[n-i-1])'''

'''list = [10,11,12,13,14,15]
l = []
for i in list:
    l.insert(0,i)
print(l)'''

#6.Display numbers from -10 to -1 using for loop.
'''for i in range(-10,0):
    print(i)'''

#7.Use else block to display a message “Done” after successful execution of for loop.
'''for i in range(5):
    print(i)
else:
    print("Done")'''

#8.Write a program to display all prime numbers within a range.
'''first_value = int(input("enter the first number: "))
sec_value = int(input("enter the second number: "))
for number in range(first_value,sec_value+1):
    if number > 1:
        for i in range(2,number):
            if(number % i) == 0:
                break
        else:
            print(number)'''

#9.Display Fibonacci series up to 10 terms.
#10.Find the factorial of a given number.(Ex:-The factorial of 5,5*4*3*2*1)
'''num = int(input("enter the number: "))
factorial = 1
if num < 0:
    print("Sorry factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)'''

#11.Reverse a given integer number.
'''num = input("enter the number: ")
i = num[::-1]
print(int(i))'''

#12.Use a loop to display elements from a given list present at odd index positions.
'''arr = [1, 2, 3, 4, 5];     
print("Elements of given array present on odd position: ");    
#Loop through the array by incrementing the value of i by 2     
for i in range(0, len(arr), 2):    
    print(arr[i]);'''

#13.Calculate the cube of all numbers from 1 to a given number.
'''number = float(input(" Please Enter any numeric Value : "))
cube = number**3
print(cube)'''

#14.Find the sum of the series upto n terms.
'''sum = 0
print("Enter the Value of n: ")
n = int(input())
print("Enter " + str(n) + " Numbers: ")
for i in range(n):
    num = int(input())
    sum = sum+num
print("Sum of " + str(n) + " Numbers = " + str(sum))'''

#15.Append new string in the middle of a given string.
'''def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)
append_middle("sravya", "teja")'''

#16.Arrange string characters such that lowercase letters should come first.
'''a=input("enter the string: ")
s="".join(sorted(a))
print(s[::-1])'''

#17.Count all letters, digits, and special symbols from a given string.
'''string = input("Enter a String : ")
alphabets=0
digits=0
special_chars=0
for i in string:
    if i.isalpha():
        alphabets += 1
    elif i.isdigit():
        digits += 1
    else:
        special_chars += 1
print("alphabets =",alphabets,"digits =",digits,"special_chars =",special_chars)'''

#18.Find all occurrences of a substring in a given string by ignoring the case.
'''string = 'Python is a very simple language'
print(string.count('a'))'''

#19.Calculate the sum and average of the digits present in a string.
'''inputString =input("Enter the string: ")
sumDigits =0
numberDigits=0
for char in inputString:
    if (char.isdigit()):
        sumDigits+=int(char)
        numberDigits+=1
average=sumDigits/numberDigits 
print(str(sumDigits))
print("%.1f" % average)'''

#20.Write a program to count occurrences of all characters within a string.
'''string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
count = 0
for i in range(len(string)):
    if(string[i] == char):
        count = count + 1
print("The total Number of Times ", char, " has Occurred = " , count)'''

#21.reverse a given string.
'''txt = input("enter the string: ")
reversed_txt = txt[::-1]
print(reversed_txt)'''

#22.Split a string on hyphens.
'''a=input("enter the string: ")
x=a.split("-")
for i in x:    
    print(i)'''

#23.Remove empty strings from a list of strings.
'''str_list = ["ram","","laxman","","hanuman",""]
print("Removing the empty spaces")
while ("" in str_list):
   str_list.remove("")
print(str_list)'''

#24.Removal all characters from a string except integers.
#25.Reverse a list in Python.
'''lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("The reversed list is ",lst)'''

#26.Concatenate two lists index-wise.
'''list1=[1,2,3,4,5,6]
list2=[2,4,6,8,5,3]
result=[]
for i in range(0, len(list1)):
    result.append(list1[i]+ list2[i])
print("Result: ",result)'''

#27.Turn every item of a list into its square.
'''my_list = [1, 2, 3, 4, 5]
squared_list = []
for number in my_list:
    squared_list.append(number**2)
print(squared_list)'''

#28.Add new item to list after a specified item.
'''list = ['I', 'programming']
list.insert(1, "love")
print(list)'''

#29.Replace list’s item with new value if found.
'''l = [ 'sravya','bunny', 'teju', 'vinnu', 'gaayu']
l[0] = 'Sravs'
print(l)'''

#30.Remove all occurrences of a specific item from a list.
mylist = [1,2,3,1,4,3,1,4,5,1,6,7,1,8,9,1,0,1]
removing_item = 1
for item in mylist:
	if(item==removing_item):
		mylist.remove(removing_item)
print(mylist)
    
