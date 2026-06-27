square = lambda x: x**2
add = lambda x,y: x+y
maximum = lambda x,y: max(x,y)
upper_case = lambda name: name.upper()

num_1 = int(input('Enter the value of the first number : '))
num_2 = int(input('Enter the value of the second number : '))

print(f'Square of the first number is : {square(num_1)}')

print(f'the sum of the two numberss id : {add(num_1 , num_2)}')

print(f'the largest of the two numbers are : {maximum(num_1, num_2)}')

name = input("enter your name : ")
print(f'Your name in upper case : {upper_case(name)}')
