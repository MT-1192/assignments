#Decorators:-By definition, a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it.
'''def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
@make_pretty
def ordinary():
    print("I am ordinary")
ordinary()'''

'''def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner
@smart_divide
def divide(a, b):
    print(a/b)
divide(2,5)
divide(2,0)''' 

'''def dec1(fun):
    def inner():
        x=fun()
        return x*x
    return inner

def dec2(fun):
    def inner():
        x=fun()
        return 2*x
    return inner
@dec1
@dec2
def n():
     return 10

print(n())'''
