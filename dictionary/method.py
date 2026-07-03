student = {"name":"Harshita","age":21,"Branch":"aiml","CGPA":8.1}
print("Name:",student["name"])
print(student.get("college"))

print(student.keys())
print(student.values())
print(student.items())

Student_1 = student.copy()
Student_1.update({"college":"SVIT"})
print(Student_1)

popped = student.pop("age")
print(f"popped item : {popped}")
print(student)

popped_1 = student.popitem()
print(f"popped item : {popped_1}")
print(student)

student.clear()
print(student)

dict_1 = {"a":"apple","b":"ball","c":"cat"}
dict_2 = {"d":"dog","e":"elephant","f":"frog"}
print(dict_1)
print(dict_2)
dict_1.update(dict_2)
print(dict_1)
print(dict_2)

print(Student_1)
Student_1.update({"CGPA":"9"})
Student_1.update({"ph":98765432})
Student_1.update({"email":"harshitaravindra1@gmail.com"})
print(Student_1)