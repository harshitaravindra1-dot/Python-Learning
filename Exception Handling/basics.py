
#problem 1
try:
    a = int(input("enter the value of a :"))
    b = int(input("enter the value of a :"))
    c = a/b
    print(f"{a}/{b}={c}")
except ZeroDivisionError:
    print("The second number cannot be 0")
except ValueError:
    print("the value must be an integer")

#problem 2
try:
    num = int(input("enter a num :"))
except ValueError:
    print("the value must be an integer")

#problem 3
numList = [1,2,3,4,5,6,7]
try:
    userIndex = int(input("enter an index value :"))
    print(numList[userIndex])
except IndexError:
    print("Index out of range")

#problem 4
try:
    f = open("txt.txt",'r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found")

#problem 5
print("Program ends")