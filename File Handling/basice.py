
f = open('File Handling/text.txt','a')
text = f.write('Hello World! ')
f.close()

f = open('File Handling/text.txt','r')
content = f.read()
print(content)
f.close()

n = open('File Handling/numbers.txt','r')
sum = 0
num_lines = 0
while True:
    num = n.readline()
    if not num:
        break
    value = int(num)
    sum += value
    num_lines +=1
n.close()
avg = sum / num_lines
print('Average:', avg)

name = open('File Handling/names.txt','r')
i=0

while True:
    contents = name.readlines()
    if not contents:
        break
    
    for j in contents:
        i+=1
        print(f"name {i}:", j)
name.close()
