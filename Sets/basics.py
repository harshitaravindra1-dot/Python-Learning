int_set = {1, 2, 3, 4, 5}
float_set = {1.1,2.2,3.3,4.4}
string_set = {"hi", "hello", "how are you"}
mixed_set = {3,5.5,"bye"}
empty_set = set()
print("int set :",int_set,"type of int set :",type(int_set))
print("float set :",float_set,"type of float set :",type(float_set))
print("string set :",string_set,"type of string set :",type(string_set))
print("mixed set :",mixed_set,"type of mixed set :",type(mixed_set))
print("empty set :",empty_set,"type of empty set :",type(empty_set))

numbers = {1,2,3,3,4,4,5}
print(numbers)

print("Length of set :",len(numbers))
print("Largest number :",max(numbers))
print("Smallest number :",min(numbers))
print("Sum of numbers :",sum(numbers))
total = sum(numbers)
avg = total/len(numbers)
print("Average :",avg)
#print(numbers[0])# TypeError: Sets are unordered collections and do not support indexing.

numbers = [1,2,2,3,4,4,5]

print("Original List :", numbers)

unique_set = set(numbers)
print("Converted to Set :", unique_set)

unique_list = list(unique_set)
print("Back to List :", unique_list)