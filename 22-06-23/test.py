'''num = int(input("enter a number: "))
sum = 0
while(num > 0):
       sum += num
       num -= 1
print("The result is", sum)'''

'''dic = {}
dic["name"] = "sravya"
dic["age"] = 24
print(dic)'''

'''def outer():
    def inner(x,y):
        print(x + y)
    inner(10,20)
outer()'''

'''string = "i love programming"
s = string.split()[::-1]
print(" ".join(s))'''

'''l = ("apple","banana","grapes")
x = "-".join(l)
print(x)'''

'''s=input("enter the string: ")
sum = 0
for i in s:
    if (i.isdigit()):
        sum += int(i)
print(str(sum))''' 

#default argument.(default arguments should follow non default arguments)
'''def f(x,y=20):
    print(x)
    print(y)
f(10)'''

#positional arguments(the order matters)
'''def f(a,b):
    print(a,b)
f(10,20)'''

#keyword arguments(order does nt matter)
'''def f(name,age):
    print(name,age)
f(name = "sravya",age=24)
f(age=24,name="sravya")'''

#keyword argument should follow positional arguments
'''def f(wish,name,age,):
    print(wish,name,age,)
f("developer",name = "sravya",age=24)'''

#variable length positional arguments
'''def f(*b):
    sum = 0
    for i in b:
        sum = sum+i
    return sum
print(f(1,2,3,4,5))
print(f(10,20))'''

#variable length keyword arguments(kwargs)
def f(**b):
    result = ""
    for i in b.values():
        result += i
    return result
print(f(a="apple ",b="is ",c="a good",d="fruit"))









    
    