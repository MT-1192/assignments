#Nested function: A function which is defined inside another function is known as inner function or nested function.
#The closure process is called encapsulation.

'''def outer():
    print("outer function starts")
    def inner():
        print("inner function executes")
        print("aman")
    def inner():
        print("inner function executes")
        print("sravs")
    print("outer function returning inner function")
    return inner
a=outer()
a()'''

'''def outer():
    print("Hii I am the outer function")
    def inner():
        print("Hii I am the inner function")
    inner()
outer()'''

'''def greet(name):
    def display_name():
        print("Hi",name)
    display_name()
greet("sravs")'''


'''def wish(firstname):
    def name():
        return firstname
    print("Hii, "+ name() + "!")
wish("sravya")'''
    

'''def num1(x):
    def num2(y):
        return x + y
    return num2
print(num1(10)(25))'''

'''def f1():
    a = "I love programming"
    def f2():
        a = "I hate programming"
        print(a)
    f2()
    print(a)
f1()'''

'''def greet():
    name="sravs"
    return lambda:"Hiii " + name
msg = greet()
print(msg())'''

'''def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1)+(n-2)
n=int(input("enter the number: "))
result = fibonacci(n)
print(result)'''

'''def calculate():
    num = 1
    def inner_func():
        nonlocal num 
#nonlocal keyword is used to work with variables inside nested functions,where the variables should not belong to inner function.
# using the keyword nonlocal to declare that the variable is not local.
        num += 2
        return num
    return inner_func
odd = calculate()
print(odd())
print(odd())
print(odd())
print(odd())
print(odd())'''

'''def make_multiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier
t1 = make_multiplier_of(3)
t2 = make_multiplier_of(5)
print(t1(9))
print(t2(3))'''

'''list = [0,1]
for i in range(1,9):
    list1=list[-1]+list[-2]
    list.append(list1)
print(list)'''

