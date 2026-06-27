def palindrome(text):
    text = text.strip().lower()
    if text == text[::-1]:
        print("text is palindrome")
    else:
        print("text is not palondrome")
text = input("enter text : ")
palindrome(text)