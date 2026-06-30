numbers = (10, 20, 30, 40, 50, 60, 70)

print("First element :",numbers[0])
print("Second element :",numbers[1])
print("Last element :",numbers[-1])
print("Second last element :",numbers[-2])
mid = len(numbers)//2
if len(numbers)%2 == 0:
    print("Middle elements :",numbers[mid-1:mid+1])
else:
    print("Middle element :",numbers[mid])

for i in numbers:
    print(i)

for i in range(len(numbers)):
    print(f"Index {i}",numbers[i])

user_index = int(input("Enter a index :"))
if 0 <= user_index < len(numbers):
    print(f"Element in index {user_index} : {numbers[user_index]}")
else:
    print("Index out of range")

user_item = int(input("Enter a value to search on the tuple :"))
if user_item in numbers:
    for i in range(len(numbers)):
        if numbers[i] == user_item:
            print(f"Found at index {i}")
else:
    print("Element not found in tuple")