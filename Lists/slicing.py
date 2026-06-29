numbers = [10, 20, 30, 40, 50, 60, 70]

print("First three elements :",numbers[:3])
print("Last 3 elements :",numbers[-3:])
mid_3 = len(numbers)//2
if len(numbers)%2 == 0:
    print("Middle 3 elements :",numbers[mid_3-1:mid_3+2])
else:
    print("Middle elements",numbers[mid_3-1:mid_3+2])

print("Reverse of list :",numbers[::-1])

print("Every 2nd element of the list :",numbers[::2])
print("Every 3rd element of the list :",numbers[::3])

start_index = int(input("Enter the start index :"))
end_index = int(input("Enter end index :"))
if start_index > end_index:
    print("Start index should be less than or equal to end index.")
if start_index < len(numbers) and end_index < len(numbers):
    print("Slice of list :",numbers[start_index:end_index])
else:
    print("Index not in range")

for i in range(-1,-len(numbers)-1,-1) :
    print(f"Index {i}: {numbers[i]}")


