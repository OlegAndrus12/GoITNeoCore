
# outer
def calculator(a, b, operation):
    message = "first level"
    
    # inner
    def add(a, b):
        nonlocal message
        message = "second level"
        print(message)
        return a + b
    

    def substract(a, b):
        return a - b
    
    
    if operation == "+":
        print(message)
        res = add(a, b)
        print(message)
        return res
    elif operation == "-":
        return substract(a, b)
    else:
        return "Incorrect operation"


a = calculator(1, 5, "+")
print(a)



a = 1
 
# Uses global because there is no local 'a'
def f():
    print('Inside f() : ', a)
 
# Variable 'a' is redefined as a local
def g():
    a = 2
    print('Inside g() : ', a)
 
# Uses global keyword to modify global 'a'
def h():
    global a
    a = 3
    print('Inside h() : ', a)
 
 
# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)


# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)


# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()