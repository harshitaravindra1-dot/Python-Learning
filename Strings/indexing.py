text = "Artificial Intelligence"
print("First Character :",text[0])
print("Last Character :",text[-1])
print("Fifth Character :",text[4])
print("Second Last Character :",text[-2])

text_2 = input("enter a string : ")
print("First character:",text_2[0])
print("Second character :",text_2[1])
print("Second last character :",text_2[-2])
print("Last character:",text_2[-1])

"""length = len(text_2)
mid = length / 2
middle = int(mid)
mid_int=length // 2
if  mid - 0.5 == mid_int :
    print("Middle term :",text_2[middle])

else:
    print("Middle terms :",text_2[middle-1:middle+1])"""

length =  len(text_2)
mid = length // 2
if length % 2 == 0:
    print("Middle terms : ",text_2[mid-1:mid+1])

else:
    print("Middle term : ",text_2[mid])


for i in text_2:
    print(i)



