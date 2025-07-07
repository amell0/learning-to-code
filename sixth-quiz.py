test = input("Enter the string you wanna test:\n")
if test == test[::-1]:
    print("This word is a palindrome!")
else:
    print("This word isn't a palindrome :(")