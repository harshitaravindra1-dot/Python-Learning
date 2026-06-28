#-------------------------------------------------------------------------
#Problem 1
user = input("Enter an string :")
print("Frist chatacter :",user[0])
print("Lats character :",user[-1])

lenght = len(user)
mid = lenght//2
if lenght % 2 == 0 :
    print("middle terms :",user[mid-1:mid+1])
else:
    print("Middle term :",user[mid])

#-------------------------------------------------------------------------
#Problem 2

print("Reverse :",user[::-1])

#-------------------------------------------------------------------------
#Problem 3

vowles = "aeiou"
vowles_count = 0
for i in user.lower():
    for j in vowles:
        if i == j:
            vowles_count += 1 

print("Number of vowles :",vowles_count)

#-------------------------------------------------------------------------
#program 4

print("Number of spaces :",user.count(" "))

#-------------------------------------------------------------------------
#program 5

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper_count = 0
for i in user:
    for j in upper_case:
        if i == j:
            upper_count += 1 

print("Number of upper cases :",upper_count)

#-------------------------------------------------------------------------
#problem 6

lower_case = "abcdefghijklmnopqrstuvwxyz"
lower_count = 0
for i in user:
    for j in lower_case:
        if i == j:
            lower_count += 1 

print("Number of lower cases :",lower_count)

#-------------------------------------------------------------------------
#problem 7

print("Replaces string",user.replace(" ","-"))

#-------------------------------------------------------------------------
#problem 8
user_sentence = input("enter a sentence :")
user_letter = input("Enter a letter :")
print(f"Does {user_sentence} start with {user_letter} ? : {user_sentence.startswith(user_letter)}")

#-------------------------------------------------------------------------
#problem 9

user_file = input("enter a file :")
python_file = ".py"
if user_file.endswith(python_file):
    print("The file is a python file")

else:
    print("The file is not a python file")

#-------------------------------------------------------------------------
#program 10

words = user_sentence.split(" ")
print("total words ",len(words))
print("Total charecters :",len(user_sentence))
word_length = []
for i in words:
    word_length.append(len(i))
maximum = max(word_length)
index_1 = word_length.index(maximum)
print("The largest word is :", words[index_1])


    

