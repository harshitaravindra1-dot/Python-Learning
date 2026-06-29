# -------------------------------
# List Methods in Python
# -------------------------------

numbers = [10, 20, 30, 40]

# -------------------------------
# reverse() vs [::-1]
# -------------------------------

print("Original List :", numbers)

print("Using slicing [::-1] :", numbers[::-1])   # Returns a reversed copy
print("Original list after slicing :", numbers)  # Original list remains unchanged

numbers.reverse()                               # Reverses the original list
print("After reverse() :", numbers)

# -------------------------------
# append()
# -------------------------------

numbers.append(50)                              # Adds an element to the end
print("After append() :", numbers)

# -------------------------------
# insert()
# -------------------------------

numbers.insert(2, 25)                           # Inserts 25 at index 2
print("After insert() :", numbers)

# -------------------------------
# extend()
# -------------------------------

more_numbers = [60, 70, 80]

numbers.extend(more_numbers)                    # Adds each element of another list
print("After extend() :", numbers)

# -------------------------------
# remove()
# -------------------------------

numbers.remove(30)                              # Removes the first occurrence of 30
print("After remove() :", numbers)

# -------------------------------
# pop()
# -------------------------------

removed = numbers.pop()                         # Removes the last element
print("After pop() :", numbers)
print("Removed element :", removed)

removed = numbers.pop(2)                        # Removes the element at index 2
print("After pop(2) :", numbers)
print("Removed element :", removed)

# -------------------------------
# sort()
# -------------------------------

numbers_2 = [50, 20, 10, 40, 30]

print("\nOriginal numbers_2 :", numbers_2)

numbers_2.sort()                                # Sorts in ascending order
print("Ascending order :", numbers_2)

numbers_2.sort(reverse=True)                    # Sorts in descending order
print("Descending order :", numbers_2)

# -------------------------------
# count()
# -------------------------------

numbers_3 = [10, 20, 20, 30, 20]

print("\nCount of 20 :", numbers_3.count(20))

# -------------------------------
# index()
# -------------------------------

print("Index of 30 :", numbers_3.index(30))

# -------------------------------
# copy()
# -------------------------------

numbers_4 = numbers_3.copy()                    # Creates a separate copy

numbers_4.append(50)

print("\nOriginal List :", numbers_3)
print("Copied List :", numbers_4)

# -------------------------------
# clear()
# -------------------------------

numbers_4.clear()                               # Removes all elements
print("After clear() :", numbers_4)