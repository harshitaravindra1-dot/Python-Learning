numbers = [10 , 20 , 30]
prices = [10.5, 20.99, 5.75]
names = ["Alice", "Bob", "Charlie"]
mixed = [10,"Python", 3.14, True]
empty = []

print("Numbers :", numbers)
print("Prices :", prices)
print("Names :", names)
print("Mixed :", mixed)
print("Empty :", empty)

print("length of numbers",len(numbers))
print("length of prices",len(prices))
print("length of names",len(names))
print("length of mixed",len(mixed))
print("length of empty",len(empty))


print("Largest number of list numbers :",max(numbers))
print("Smallest number of list numbers :",min(numbers))
print("Sum of number of list numbers :",sum(numbers))

average = sum(numbers) / len(numbers)
print("Average number of list numbers :",average)

print("Type of list numbers :",type(numbers))
print("Type of list prices :",type(prices))
print("Type of list names :",type(names))
print("Type of list mixed :",type(mixed))
print("Type of list empty :",type(empty))

languages = ["Python", "Java", "C","C++"]
print("First language :",languages[0])
print("Last language :",languages[-1])
if len(languages) % 2 == 0:
    mid = len(languages)//2
    print("Middle languages :",languages[mid-1:mid+1])
else:
    mid= len(languages)//2
    print("Middle language :",languages[mid])
print("Total languages :",len(languages))

marks = [90, 80, 70, 60, 50]
marks.append(80)
print("After append :", marks)
marks.insert(3,75)
print("After insert :", marks)
marks.remove(60)
print("After remove :", marks)
popped = marks.pop(1)
print("After pop marks :",marks)
print("Popped element :",popped)