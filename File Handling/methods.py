f = open("File Handling/program.txt", "r")
content = f.read()
print("contents of program.txt :\n",content)
f.close()

g = open("File Handling/program.txt","a")
g.write("\nkannada\nhindi\n")
g.close()

with open("File Handling/program.txt","w")as h:
    h.write("javascript\ndjango\nfastapi\n")

i = open("File Handling/num2.txt","r")

greatest = 0
smallest = 100000
total = 0
while True:
    j = i.readlines()
    
    if not j:
        break
    for l in j:
        k = int(l)
        if k > greatest:
            greatest = k

        if k < smallest:
            smallest = k
        
        total += k

        avg = total / len(j)

print("grestest num :",greatest)
print("smallest num :",smallest)
print("Sum :",total)
print("Avg :",avg)

#problem 5
with open("File Handling/student_names.txt",'r')as p:
    names = p.readlines()
    print("number of studens :",len(names))

#problem 6 and 7
word_count = 0
python_count = 0
with open("File Handling/paragraph.txt",'r')as para:
    while True:
        line = para.readlines()
        print(line)
        if not line:
            break
        number_lines = len(line)
        for phrase in line:
            word = phrase.split(" ")
            word_count += len(word)
            for string in word:
                if string.lower() == "python":
                    python_count += 1
print("Number of words :",word_count)
print("Number of lines :",number_lines)
print("number of python in paragraph :",python_count)

#problem 8
highest = 0
total = 0
with open("File Handling/marks.txt","r") as b:
    no_of_students = 0 
    while True:
        line = b.readlines()
        
        if not line:
            break
        for i in line:
            no_of_students += 1
            print(i)
            student = i.split(",")
            print(student)
            name = student[0]
            marks = int(student[1])
            if marks > highest:
                highest = marks
                topper = name
            
            total += marks
    avg = total /no_of_students
    print(f"Highest marks is scored by {topper}")
    print("Average marks :",avg)
 
