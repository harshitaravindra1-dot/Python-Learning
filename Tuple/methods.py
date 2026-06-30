numbers = (10, 20, 20, 30, 20, 40)

print("Count of 20 :",numbers.count(20))
print("Count of 30 :",numbers.count(30))
print("Count of 40 :",numbers.count(40))

num = (10, 20, 20, 30, 40, 50)
print("Index of 30 :",num.index(30))
print("Index of 10 :",num.index(10))
print("Index of 50 :",num.index(50))

user_item = int(input("Enter an item :"))
if user_item in num:
    for i in range(len(num)):
        if user_item == num[i]:
            print(f"Index = {i}")
else:
    print("Item not found")

user_count = int(input("Enter the element you want to count :"))
count = 0
for i in numbers:
    if i == user_count:
        count += 1

print(f"The number of times {user_count} occured : {count}")