

numbers = (12, 145, 67, 23, 89, 94)

#problem 1
greatest = numbers[0]
for i in numbers:
    if greatest < i:
        greatest = i
print("Greatest number :",greatest)

#problem 2
smallest = numbers[0]
for i in numbers:
    if smallest > i:
        smallest = i
print("Smallest number :",smallest)

#problem 3
num_list = list(numbers)
num_list.remove(greatest)
greatest_2 = num_list[0]
for i in num_list:
    if greatest_2 < i:
        greatest_2 = i
print("Greates number :",greatest_2)

#problem 3
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even elements :",even_count)
print("Number of odd elements :",odd_count)

#problem 5

user_item= int(input("Enter the item you want to search :"))
if user_item in numbers:
    for j in range(len(numbers)):
        if numbers[j] == user_item:
            print(f"{user_item} found in : {j}")
else:
    print("Item not found")

#problem 6
int_numbers = (2, -4, 6, -1, -7, 9)
positive = []
negative = []
for i in range(len(int_numbers)):
    if int_numbers[i] >= 0:
        positive.append(int_numbers[i])
    else:
        negative.append(int_numbers[i])

print("Positive elements :",positive)
print("Negative elements :",negative)

#problem 7
num_3 = (10,20,30)
num_list = list(num_3)
num_list.append(40)
num_list.remove(30)

num_3 = tuple(num_list)
print("New tuple :",num_3)

#problem 8
num_4 = (10, 70, 90, 30, 80)
greater_50 = 0
for i in num_4:
    if i > 50:
        greater_50 += 1
print("Numbers greater than 50 :",greater_50)

#problem 9
add = 0
for i in numbers:
    add += i

avg = add / len(numbers)
print(f"Average of {numbers} :",avg)
