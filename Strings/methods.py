a = "python is great python"
b = ['python','is','great']
c = "!!!!!!!python!!!!!"
print(a.upper()) #conevrts all teh charecters to upper case
print(a.lower()) #converts all the charecters to lower case
print(a.title()) #only the first letter or each word in the shring is in upper case and the remaining will be in lower case 
print(a.capitalize()) #only the first letter of the string is in upper case 
print(a.swapcase()) #all the charecters in upper case is converted to lower case and the charecters in lower case is converted to upper case 
print(a.replace("great","good")) # finds a sequence of charecters and replaces it with andther sequence
print(a.count("python")) #counts the number of times a sequence repeats
print(a.startswith("th",2,10)) #goes to the specific index and checks if that sequence start with the specific string
print(a.endswith("on",0,6)) #goes to the specific index and checks if that sequence ends with the specific string
print(a.split(" ")) #Splits the string into a list using the specified separator
print(" ".join(b)) #Joins the elements of an iterable into a string using the specified separator
print(a.isalpha()) #checks if the string has only aplhabets
print(a.isdigit()) #checks if the string has only digits
print(a.isalnum()) #checks if the string has only alphabets and digits
print(len(a)) #returns the lengeth of the string
print(c.strip("!"))# Removes specific characters from the beginning and end of the string.



