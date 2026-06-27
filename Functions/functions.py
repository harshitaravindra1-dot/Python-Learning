def greet(person="Human"):
    print(f"welcome {person} to python programming")

def display_name(name):
    print(f'Hello {name}!!')

def add(x,y):
    return x+y

def area(x,y):
    return x*y

def student(name,age,course):
    print(f'{name} is {age} years old and is studying {course}')


def calculator(m,n,operator):

    if operator == '+':
        return m+n
    
    elif operator == "-":
        return m-n
    
    elif operator == "*":
        return m*n
    
    elif operator == '/':
        if n == 0:
            return "n cannot be 0"

        else:
            return m/n
        
    else:
        return 'you did not enter a valid operator'

greet()

user= input("enter your name:\t")
display_name(user)

a = int(input("enter the value of a:\t"))
b = int(input("enter the value of b:\t"))

sum=add(a,b)
print(f'sum {a} + {b} : {sum}')

A=area(a,b)
print(f'area of {a} and {b} : {A}')

student(age=21, course="BE", name="Anna")

op=input("enter the operation you want to perform ( + , - , * , / ):\t")
cal=calculator(a,b,op)
print(f'the resut of the calculation = {cal}')


