#problem 1
list_1 = [1,2,3,3,4,4]
list_2 = list(set(list_1))
print("list 1 :",list_1)
print("list 2 :",list_2)

#problem 2
a = {"a","b","c","d"}
b = {"c","d","e","f"}

print("union of both sets :",a.union(b))
print("intersection of both sets :",a.intersection(b))
print("elements only in the first collection :",a.difference(b))
print("elements only in the second collection :",b.difference(a))
print("elements that belong to exactly one collection :",a.symmetric_difference(b))

#problem 3
unique_count = 0
unique_set = set()
for i in range(5):

    user_input = int(input("enter a value :"))
    unique_set.add(user_input)
print("number of unique values :",len(unique_set))

#problem 4
python = {"harshita","aayush","rishitha","hima"}
ai = {"harshita","aayush","shamita","shreeya"}


print("Students enrolled in both courses :",python.intersection(ai))
print("Students enrolled only in Python. :",python.difference(ai))
print("Students enrolled only in AI. :",ai.difference(python))
print("Total unique students :",python.union(ai))

#problem 5
total_students = ai.union(python)
ds = {"arun","yashu","bindhu"}
print("are students in python in total_students :",python.issubset(total_students))
print("are students in ds in total_students :",ds.issubset(total_students))

#problem 6
print("are students in python also students in ai :",python.isdisjoint(ai))
print("are students in ds also students in ai :",ds.isdisjoint(ai))

#problem 7
sentence = input("enter a string :")
ls = str.split(" ")
set1 = set(ls)
print("number of unique words :",len(set1))

#problem 8
set3 = {1,2,3,4}
set4 = {3,4,5,6,1}
set5 = set()
for i in set3:
    for j in set4:
        if i == j:
            set5.add(i)
print(set5)

#problem 9
A = {1,2,3,4,5,6,7}
B = {4,5,6,7,8}
half_A = len(A) // 2
C = set()
for i in A:
    for j in B:
        if i == j:
            C.add(i)
if len(C) > half_A:
    print("the sets are mostly common")
else:
    print("the sets are mostly different")

