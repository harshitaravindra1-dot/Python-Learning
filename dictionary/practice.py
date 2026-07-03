#problem 1
student_marks = {"harshita":100,"shamita":85,"roopa":70,"ravindra":99}
highest = max(student_marks.values())
for key in student_marks.keys():
    if student_marks[key] == highest:
        print(f"highest marks {highest} scored by {key}")


#problem 2
student_details = {"name":None,"age":None,"branch":None,"cgpa":None}
for key in student_details.keys():
    value = input(f"enter the student {key} :")
    student_details.update({key:value})
print(student_details)

#problem 3
product =  {"fan":1000,"computer":15000,"tv":12000,"fridge":20000}
user = input("Enter the product name :")
if product.get(user) == None:
    print("Item not found")
else:
    print(f"Coset of {user} : {product[user]}")

#problem 4
countries = {"india":"delhi","japan":"tokyo"}
for key in countries.keys():
    print(f"{key}'s capital is {countries[key]}") 

#problem 5
math = {"harshita":100,"shamita":85,"roopa":70,"ravindra":99}
science = {"alex":100,"aayush":70,"rishitha":79,"hima":90}
math.update(science)
print(math)

#problem 6
above_80 = 0
for value in math.values():
    if value > 80:
        above_80+=1
print("number of students who have scored above 80 :",above_80)

#problem 7
list_students = {"harshita":[100,100,100],"shamita":[90,80,70],"roopa":[80,99,89],"ravindra":[90.70,89]}
for key in list_students.keys():
    avg = sum(list_students[key]) / len(list_students[key])
    print(f"average marks of {key} : {avg}")

#problem 8
user_sentence = input("enter a sentence :")
user_list = user_sentence.split(" ")
sentence_dict = {}
print(user_list)
for i in user_list:
    if i in sentence_dict.keys():
        sentence_dict.update({i:sentence_dict[i]+1})
    else:
        sentence_dict.update({i:1})
print(sentence_dict)
