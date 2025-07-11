import random

length = int(input("Enter the length of your password: "))

# to be honest, i got some help with this one
alphabet = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
symbols = '!@#$%^&*()' 

content = alphabet + alphabet.upper() + numbers + symbols  

with open("base.txt", "a+") as file:
    file.write(content + "\n")  
    
    password = ''.join(random.choice(content) for _ in range(length))
    print("Generated Password:", password)
    