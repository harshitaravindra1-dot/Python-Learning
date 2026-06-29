num = [12, 145, 67, 23, 89, 94]

#greatest num
greatest = num[0]

for i in num:
    if i > greatest:
        greatest = i

print(greatest)

#lowest
lowest = num[0]

for i in num:
    if i < lowest:
        lowest = i
print(lowest)

#sum and average
add=0
for i in num:
    add += i

print("Sum :",add)
avg = add / len(num)
print("Average :",avg)

#odd and even 
odd_count=0
even_count=0
for i in num:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even =",even_count)
print("Odd =",odd_count)

#second largest

num_copy=num.copy()
num_copy.remove(greatest)
greatest_2 = num_copy[0]
for i in num_copy:
    if i > greatest_2:
        greatest_2 = i
print("Second greatest :",greatest_2)

#remove duplicate elements
exp = [1,2,2,3,4,4,5]
for i in exp:
    c = exp.count(i)
    if c > 1:
        for j in range(c-1):
            exp.remove(i)
print(exp)

#find
numbers = [10,20,30,20,40]
x=int(input("ente a number to find in the list :"))
if x not in numbers:
    print("Element is not prestent in the list")
else:
    for k in range(len(numbers)):
        if x == numbers[k]:
            print(f"{x} found at {k}")

# positive and negitive
int_num = [2,-4,6,-1,-7,9]
positive =[]
negitive = []
for item in int_num:
    if item >= 0:
        positive.append(item)
    else:
        negitive.append(item)
print("Positive numbers :",positive)
print("Negitive numbers :",negitive)

#rotate to the right

rotate = [10,20,30,40]
rotate_copy = rotate.copy()
for i in range(len(rotate)):
    if i != 0:
        rotate[i] = rotate_copy[i-1]
    else:
        rotate[i] = rotate_copy[-1]
print(rotate)

#student marks
marks = []
for i in range(5):
    m=int(input(f"Enter the marks of student {i} :"))
    marks.append(m)
print("List of marks :",marks)

maximum_marks = marks[0]
for i in marks:
    if i > maximum_marks:
        maximum_marks = i
print("Maximum marks :",maximum_marks)

lowest_marks = marks[0]
for i in marks:
    if i < lowest_marks:
        lowest_marks = i
print("Lowest marks :",lowest_marks)

total_marks = 0

for mark in marks:
    total_marks += mark

average_marks = total_marks / len(marks)


print("Average marks :",average_marks)

fail_count = 0
pass_count = 0
for item in marks:
    if item < 35:
        fail_count += 1
    else:
        pass_count += 1
print("Number of passed students :",pass_count)
print("Number of failed students :",fail_count)
