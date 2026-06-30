int_tup = (1,2,3,4,5)
float_tup = (1.2,2.3,3.4,4.5,5.6)
string_tup = ("apple", "banana", "cherry", "date", "elderberry")
mixed_tup = (1,2,3,3.14,5.5,"harshita")
empty_tup = ()
single_tup = (1,)

print("integer tuple :",int_tup,type(int_tup))
print("Float tuple :",float_tup,type(float_tup))
print("String tuple :",string_tup,type(string_tup))
print("Mixed tuplr",mixed_tup,type(mixed_tup))
print("Empty tuple :",empty_tup,type(empty_tup))
print("Single element tuple :",single_tup,type(single_tup))

print("Length of tuple :",len(int_tup))
print("Largest num in tuple :",max(int_tup))
print("Smallest num in tuple :",min(int_tup))
sum_tup = sum(int_tup)
avg_tup = sum_tup/len(int_tup)
print("Sum of integer tuple :",sum_tup)
print("Average of integer tuple :",avg_tup)

lang = ("Python", "Java", "C++", "JavaScript")
print("First language :",lang[0])
print("Last language :",lang[-1])
mid = len(lang)//2
if len(lang)%2 == 0:
    print("Middle terms :",lang[mid-1:mid+1])
else:
    print("Middle term :",lang[mid])
print("Total languages :",len(lang))


numbers = (10, 20, 30)
numbers[0] = 100 #gives typeerror because tuple is immutable , to manipulate a tuple we should first convert it to a list then make changes on that tist and them convert the list to a tuple