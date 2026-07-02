student = {1:"John", 2:"Alice", 3:"Bob", 4:"Eve"}
books = {1:"Math", 2:"Science", 3:"History", 4:"Art"}
emp = {1:"Manager", 2:"Engineer", 3:"Technician", 4:"Clerk"}
empty = {}
print("Student Dictionary and type:", student, type(student))
print("Books Dictionary and type:", books, type(books))
print("Employee Dictionary and type:", emp, type(emp))
print("Empty Dictionary and type:", empty, type(empty))

stu_1 = {'name':'Harshita', 'age':21, 'Branch':'aiml','CGPA':8.1}

print(stu_1.values())

print("Length of Student Dictionary:", len(stu_1))
print("Keys of Student Dictionary:", stu_1.keys())
print("Values of student dictionary :",stu_1.values())

mobile = {'brand':'Apple', 'model':'iPhone 13', 'price':799, 'color':'Black'}
print(mobile)
mobile.update({'brand':'samsung'})
mobile.update({'ram':'8GB'})
print(mobile)

s1={5:"harshita",6:"shamita",7:"roopa",8:"ravindra"}
student.update(s1)
print(student)