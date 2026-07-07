#problem 1
try:
    a = int(input("enter the value of a :"))
    b = int(input("enter the value of b :"))
except ValueError:
    print("the values must be integers")
else:
    total = a+b
    print("Sum of two numbers :",total)
finally:
    print("SUm problem complete")

#problem 2
fruits = ['apple','mango','banana','orange']
try:
    userIndex = int(input("enter the index :"))
    print(fruits[userIndex])
except IndexError:
    print("Index is not valid")
except ValueError:
    print("Index must be an integer")

#problem 3
fileName = input("Enter the file name :")
try:
    f = open(fileName)
except FileNotFoundError:
    print("File not found")
else:
    contents = f.read()
    print(contents)
finally:
    print("File search problem complete")

#problem 4
student = {"harshita":90,"shamitha":80,"roopa":70,"ravindra":99}
try:
    userKey = input("Enter student name :")
    ans = student[userKey]
except KeyError:
    print("Student not found")
else:
    print("Marks of student :",ans)
finally:
    print("dictionary search problem complete")

#problem 5
total = 0
count = 0
while True:
    try:
        while True:
            number = input("enter a number:")
            if number.lower() == 'stop':
                break
            intNum = int(number)
            total += intNum
            count += 1
        if number.lower() == 'stop':
            break
    except ValueError:
        print("Type stop to stop or enter a number")
if count > 0:
    print("Sum of numbers :",total)
    avg = total / count
    print("Total numbers entered :",count)
    print("Average of numbers :",avg)

#problem 6
total = 0
count = 0
with open("Exception Handling/numbers.txt")as f:
    
    while True:
        try:
            lines_list = f.readline()
            if not lines_list:
                break
            num = int(lines_list)
            total += num
            count += 1
        except ValueError:
            print("Operaction can only be preformed on int")
if count > 0:
    print("Sum of numbers :",total)
    avg = total / count
    print("Total numbers entered :",count)
    print("Average of numbers :",avg)

#problem 7
while True:
    try:
        userInput = int(input("1. Divide two numbers\n2. Find a list element\n3. Open a file\n4. Exit :"))

        if userInput == 1:
            try:
                a = int(input("enter the value of a :"))
                b = int(input("enter the value of a :"))
                c = a/b
                print(f"{a}/{b}={c}")
            except ZeroDivisionError:
                print("The second number cannot be 0")
            except ValueError:
                print("the value must be an integer")

        elif userInput == 2:
            fruits = ['apple','mango','banana','orange']
            try:
                userIndex = int(input("enter the index :"))
                print(fruits[userIndex])
            except IndexError:
                print("Index is not valid")
            except ValueError:
                print("Index must be an integer")

        elif userInput == 3:
            try:
                f = open("txt.txt",'r')
                content = f.read()
                print(content)
            except FileNotFoundError:
                print("File not found")
        elif userInput == 4:
            break
        else:
            raise Exception
    except Exception:
        print("Choose the numbers in the menu")
    
