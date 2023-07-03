#1.solid rectangle
'''a=int(input("enter the rows: "))
b=int(input("enter the columns: "))
counter=0
while counter<a:
    print(" * " * b)
    counter=counter+1'''

#2.solid right angled triangle
'''n=int(input("enter the rows: "))
for i in range(n):
    print("* " * (i+1))'''


#3.solid square
'''n=int(input("enter the rows: "))
for i in range(n):
    print("* " * n)'''

#4.square with numbers
'''number = int(input("enter the rows: "))
counter = 1
while counter <= number:
    row = str(counter) * number
    print(row)
    counter = counter + 1'''

#5.Inverted right angled triangle
'''n=int(input("enter the rows: "))
for i in range(n):
    print("* " * (n-i))'''

#6.Right angled triangle
'''rows = int(input("enter the rows: "))
#Building the Triangle Rows
for num in range(1, rows + 1):
    spaces = "  " * (rows - num)
    stars = "* " * num
    print(spaces + stars)'''

#7.pyramid with numbers
'''rows = int(input("enter the rows: "))
for r in range(rows):
    spaces = "  " * (rows - r - 1)
    string = (str(r  + 1) + " ") * ((2 * r) + 1)
    each_row = spaces + string
    print(each_row)'''

#8.pyramid with stars
'''rows = int(input("enter the rows: "))
for r in range(rows):
    spaces = "  " * (rows - r - 1)
    stars = "* " * ((2 * r) + 1)
    each_row = spaces + stars
    print(each_row)'''

#9.inverted right angled triangle with numbers.
'''n=int(input("enter the rows: "))
for i in range(n):
    number = n - i
    row = (str(number) + " ")*number
    print(row)'''

#10.inverted pyramid
'''number_of_rows = int(input("enter the rows: "))
for row in range(number_of_rows):
    spaces = " " * row
    stars = "*" * (2 * (number_of_rows - row) - 1)
    each_row = spaces + stars
    print(each_row)'''

#11.pyramid-2
'''number = int(input("enter the rows: "))
for each_number in range(number):
    stars = "* " * (each_number + 1)
    print(stars)
for each_number in range(number):
    stars = "* " * (number - each_number - 1)
    print(stars)'''

#12.diamond
'''n=int(input("enter the rows: "))
k = n-1
for i in range(1, n+1):
    spaces = " " * k
    stars = "* " * i
    print(spaces+stars)
    k = k - 1
k=n-1
for i in range(1,n):
    stars = "* " * k
    spaces = " " * i
    print(spaces+stars)
    k = k - 1'''

#13.diamond with numbers
'''num= int(input("Enter the number :"))
for i in range(1,num+1):
    count=1
    string=""
    for j in range(1,i+1):

        string+=str(count)+" "
        count+=1
    print(" "*(num-i)+ string)    
for i in range(1,num):
    count=1
    string=""
    for j in range(1,(num-i)+1):
        string+=str(count)+" "
        count+=1 
    print(" "*i+ string)'''

#14.diamond
'''num= int(input("Enter the number :"))
count=1
for i in range(1,num+1):
    string=""
    for j in range(1,i+1):

        string+=str(count)+" "
        count+=1
    print(" "*(num-i)+ string)    
for i in range(1,num):
    string=""
    for j in range(1,(num-i)+1):
        string+=str(count)+" "
        count+=1 
    print(" "*i+ string)'''

#15.hollow square
'''n=int(input("enter the rows: "))
for i in range(n):
  if (i == 0) or (i == (n - 1)):
    print("* " * n)
  else:
    number_of_spaces = ("  " * (n - 2))
    print("* " + number_of_spaces + "* ")'''

#16.hollow rectangle
'''m=int(input("enter the rows: "))
n=int(input("enter the columns: "))
for i in range(m):
    if (i==0) or (i == m-1):
        print("* " * n)
    else:
        number_of_spaces = ("  " * (n - 2))
        print("* " + number_of_spaces + "* ")'''

#17.hollow right angled triangle
'''n = int(input("enter the rows: "))
print("* ")
for i in range(n - 2):
    hollow_spaces = " " * (2 * i)
    hollow_line = "* " + hollow_spaces + "* "
    print(hollow_line) 
star_line = "* " * n 
print(star_line)'''

#18.
'''n = int(input("enter the rows: "))
for i in range(n+1):
    print("*",end="")
print()
for i in range(n):
    print("*",end="")
    print(" "*(n-i-1),end="")
    print("*")'''

#19.
'''n=int(input("enter the rows: "))
for i in range(n):
    print("* " * (i+1))
for i in range(n):
    print("* " * (i+1))'''

#20. M pattern
'''no_of_rows = int(input("enter the number: "))
for each_number in range(1, no_of_rows + 1):
    first_triangle_stars = "* " * each_number
    first_triangle_spaces = "  " * (no_of_rows - each_number)

    first_triangle = first_triangle_stars + first_triangle_spaces
    
    second_triangle_spaces = "  " * (no_of_rows - each_number)
    second_triangle_stars = "* " * each_number

    second_triangle = second_triangle_spaces + second_triangle_stars

    print(first_triangle + second_triangle)'''

#21.
'''number = int(input("enter the numbers: "))
for each_number in range(1, number + 1):
    number_in_row = str(each_number)
    each_row = (number_in_row + " ") * each_number
    print(each_row)
for each_number in range(1, number):
    number_in_row = str(number - each_number)
    each_row = (number_in_row + " ") * (number - each_number)
    print(each_row)'''

#22.
'''number = int(input("enter the rows: "))
for each_number in range(1, number + 1):
    stars = "* " * each_number
    spaces = "  " * (2 * (number - each_number))
    each_row = stars + spaces + stars
    print(each_row)
for each_number in range(1, number):
    stars = "* " * (number - each_number)
    spaces = "  " * (2 * each_number)
    each_row = stars + spaces + stars
    print(each_row)'''

#23.hollow pyramid
'''n = int(input("enter the rows: "))
for row in range(1, n + 1):
    left_spaces_count = n - row
    left_spaces = " " * left_spaces_count
    row_output = left_spaces + "* " * row
    
    if(row == 1 or row == n):
        print(row_output)
    else:
        hollow_spaces_count = row - 2
        hollow_spaces = "  " * hollow_spaces_count
        row_output = left_spaces + "* " + hollow_spaces + "* "
        print(row_output)'''

#24.
'''n = int(input("enter the rows: ")) 
for i in range(n):
    for j in range(n):
        if i==(n-1) or j==(n-1) or i+j==(n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

#25.
'''n = int(input("enter the rows: ")) 
for i in range(0,n):
    if i == 0:
        print("* " * n)
    elif (i== n-1):
        left_spaces = "  " * (n-1)
        print(left_spaces + "*")
    else:
        left_spaces = "  " * (i)          
        hollow_spaces = "  " * (n-i-2)
        print(left_spaces+"* " +hollow_spaces + "* " )'''


