name = input("What's your name?\n")
age = int(input("How old are you?\n"))
print(f"WOAW!, your name is {name} and you're {age} old!")
cy = 2025
centy = cy + (100 - age) 
print(f"You will turn 100 at {centy}!\n")
rep = int(input("How many times do you wanna repeat the message?:\n"))
for i in range (rep) :
    print(f"You will turn 100 at {centy}!\n")