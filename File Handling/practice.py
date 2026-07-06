#problem 1
highest = 0
total = 0
lowest = 10000
passedCount = 0
failedCount = 0 
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
            if marks < lowest:
                lowest = marks
                low_student = name
            total += marks
            if marks >= 35:
                passedCount += 1
            elif marks < 35:
                failedCount += 1
    avg = total /no_of_students
    print(f"Highest marks is scored by {topper} : {highest}")
    print(f"Highest marks is scored by {low_student} : {lowest}")
    print("Average marks :",avg)
    print("Number of failed students :",failedCount)
    print("Number of passed students :",passedCount)

#problem 2
positiveNum = []
negitiveNum = []
with open("File Handling/integer.txt","r") as f:
    num_list = f.readlines()
    for i in num_list:
        num = int(i)
        if num >= 0:
            positiveNum.append(num)
        else:
            negitiveNum.append(num)
print("Positive numbers:",positiveNum)
print("Negitive numbers:",negitiveNum)

#problem 3
userName = input("Enter a name :")
line_count = 0
nameFound = False
with open("File Handling/names.txt","r") as names:
    nameList = names.readlines()
    for i in nameList:
        line_count += 1
        if i.count(userName.capitalize()) >= 1:
            print("Name found in line :",line_count)
            nameFound = True
    if nameFound == False:
        print("Name not found")
        
#problem 4
longestWord = ""
shourtestWord = ""
long = 0
short = 1000
wordCount = 0
totalWordLen = 0
with open("File Handling/paragraph.txt",'r')as para:
    line_list = para.readlines()
    for line in line_list:
        word_list = line.split(" ")
        for j in word_list:
            wordCount += 1
            totalWordLen += len(j)
            if len(j) > long:
                long = len(j)
                longestWord = j
            
            if len(j) < short:
                short = len(j)
                shourtestWord = j
avg = totalWordLen/wordCount
print("Londest word :",longestWord)
print("Shortest word :",shourtestWord)
print("Number of words :",wordCount)
print("average length of words :",avg)

#problem 5
