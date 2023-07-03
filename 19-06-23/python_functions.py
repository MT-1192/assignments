#Functions:Block of re-usable code to perform a specific action.(Re-usable code:using an existing code without writing it everytime we need.)

#1.Defining a function:The functional block of code is executed only when the function is called.
#code: 
'''def greet():
    print("Hello")
greet()'''

'''def greet():
    print("Hello")
name = input("enter the name: ")
greet()
print(name)'''

#Function with arguments:We can pass values to a function using arguments.
'''def greet(word):
    msg = "Hello " + word
    print(msg)
name = input("enter the name: ")
greet(word = name)'''

#Returning a value:
'''def greet(word):
    msg = "Hello " + word
    return msg
name = input("enter the name: ")
greeting = greet(word = name)#storing the value returned from the function
print(greeting)'''

#program
'''def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a-b
def div(a, b):
    return a/b

print("Enter Two Numbers: ", end="")
nOne = int(input())
nTwo = int(input())
print("Enter the Operator (+,-,*,/): ", end="")
ch = input()
if ch=='+':
    print("\n" +str(nOne)+ " + " +str(nTwo)+ " = " +str(add(nOne, nTwo)))
elif ch=='-':
    print("\n" +str(nOne)+ " - " +str(nTwo)+ " = " +str(sub(nOne, nTwo)))
elif ch=='*':
    print("\n" +str(nOne)+ " * " +str(nTwo)+ " = " +str(mul(nOne, nTwo)))
elif ch=='/':
    print("\n" +str(nOne)+ " / " +str(nTwo)+ " = " +str(div(nOne, nTwo)))
else:
    print("\nInvalid Operator!")'''

'''def add(a,b):
    print("Addition of two numbers", a+b)
def sub(a,b):
    print("Subtraction of Two numbers",a-b)
def mul(a,b):
    print("Multiplication of two numbers", a*b)
def div(a,b):
    print("Division of two numbers",a/b)
x=int(input("Enter first numbers: "))
y=int(input("Enter Second numbers: "))
add(x,y)
sub(x,y)
mul(x,y)
div(x,y)'''

#4 types of arguments:-1.positional 2.keyword arguments 3.variable length arguments 4.default arguments
#1.key-word arguments:-passing values by their names
'''def greet(arg_1, arg_2):
  print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(arg_1=greeting,arg_2=name)'''

#error code:-required one positional argument arg1
'''def greet(arg_1, arg_2):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(arg_2=name)'''

#2.Values can be passed without using argument names.(These values get assigned according to their position.Order of the arguments matters here.)
'''def greet(arg_1, arg_2):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(greeting,name)'''

#error code:
'''def greet(arg_1, arg_2):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(greeting)'''

'''def greet(arg_1, arg_2):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet()'''

#3.default arguments
'''def greet(arg_1="hello",arg_2="sravs"):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet()'''

'''def greet(arg_1="hii",arg_2="sravs"):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(greeting)'''

'''def greet(arg_1="hii",arg_2="sravs"):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(name)'''

'''def greet(arg_1="hii",arg_2="sravs"):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(arg_2=name)'''

'''def greet(arg_1="Hi", arg_2):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(arg_2=name)''' #error code.Non-default arguments cannot follow default arguments.

'''def greet(arg_2, arg_1="hii"):
    print(arg_1 + " " + arg_2)
greeting = input("enter the greet: ")
name = input("enter the name: ")
greet(arg_2=name)'''

 
