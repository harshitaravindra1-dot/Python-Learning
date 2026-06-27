visitor_count = 0
company_name = "Tech Solutions"
manager = 'Alice'

def visit():
    global visitor_count
    visitor_name = input("Enter your name : ")
    print(f'Office : {company_name}\nVisitor : {visitor_name}')

    visitor_count += 1
    print(f"Total visitors : {visitor_count}")

    message = "Welcome to the office!"
    print(message)
    
def display_manager():
    manager = "Bob"
    print(f'Local Manager : {manager}') # prints the local variable manager

for i in range(3):
    visit()
    print("-"*30)
 #print(message) # NameError occurs because 'message' is a local variable.
# Local variables exist only inside the function where they are created.
display_manager()
print(f'Global Manager : {manager}') #prints the global variable manager


