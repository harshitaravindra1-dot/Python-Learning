num = {1,2,3,4,5,6}
num.add(7)
print(num)
num.add(5)
print(num)

num.remove(3)
print(num)
#num.remove(8) cant remove 8 because it dosent exist in the set and throws an error

num.discard(8)#even when a value isnt present in a set it dosent throw an error

print(num)

popped = num.pop()
print("Removed value :",popped)
print(num)

num_2 = num
num_2.remove(7)
print("num :",num)
print("Num_2 :",num_2)

num_3 = num.copy() # or set(num)
num_3.add(9)
print("num :",num)
print("Num_3 :",num_3)
num_3.clear()
print(num_3)
num_3.add(11)
print(num_3)

a = {1,2,3,4,5}
b = {3,4,5,6,7}
print("union of a and b :",a.union(b))
print("intersection of a and b :",a.intersection(b))
print("valuse that are present only in set a :",a.difference(b))
print("valuse that are present only in set b :",b.difference(a))
print("values that are present in exactle one set :",a.symmetric_difference(b))
b.update(a)
print("Set b :",b)

print("is a subset of b :",a.issubset(b))
c = {10,11,12,13}
print("is c subset of b :",c.issubset(b))

print("is b a superset of a :",b.issuperset(a))
print("are sets a and c disjoint :",a.isdisjoint(c))