numbers = [12, 45, 67, 23, 89, 34, 56]

print("First element :",numbers[0])
print("Last element :",numbers[-1])
if len(numbers)%2 == 0:
    mid = len(numbers)//2
    print("Middle terms :",numbers[mid-1:mid+1])
else:
    mid = len(numbers)//2
    print("Middle term :",numbers[mid]) 

for item in numbers:
    print(item)  

for i in range(len(numbers)):
    print(f"Index [{i}] :",numbers[i])

index = int(input("Enter and index :"))
if 0 <= index < len(numbers):
    print(f"Item in index {index} : {numbers[index]}")
else:
    print("Invalid index")

user_value = int(input("enter a number :"))
if user_value in numbers:
    print(f"{user_value} found at index : {numbers.index(user_value)}")
else:
    print("Value not found")







