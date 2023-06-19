# 1.d={"don":100,"sunny":200,"sai":1,"shannu":20}
#Expected OUTPUT: 321
'''d={"don":100,"sunny":200,"sai":1,"shannu":20}
sum_of_values = sum(d.values())
print("Total=", sum_of_values)'''

# 2.Number of occurrences of each letter present in the string in Dictionary . aabbcdeaabbceder

'''n = input("Enter the string: ")
s = {}
for i in n:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
print(s)'''

# 3.Number of occurrences of each vowel present in the given string.

# Using dictionary and list comprehension
'''string = "aaaaahhhhhuuuuuiiiiibbbbbb"
string = string.lower()
count = {x:sum([1 for char in string if char == x]) for x in 'aeiou'}
print(count)'''

# 4.Write a program adding the student name and marks from keyboard and create a dict also display student marks by taking student name as input.
'''n = int(input("Enter number of students: "))  
result = {}  
for i in range(n):  
   print("Enter Details of student No.", i+1) 
   rno = int(input("Roll No: "))   
   name = input("Name: ")  
   marks = int(input("Marks: "))  
   result[rno] = [name, marks]    
print(result)'''

number = 9988
num = str(number)
size = len(num)
reverse_num = num[size::-1]
print(reverse_num) 

number = 4
for n in range(number - 1):
    print((number-n)* ' ' + (2*n+1) * "*")
for n in range(number-1, -1, -1):
    print((number - n)* ' ' + (2*n+1) * "*")

