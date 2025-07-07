num = int(input("Enter the number: "))
dlist = []

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        dlist.append(i)
print(f"The devisors are{dlist}")

number = int(input("Enter the number you wanna test: "))

if number % 2 == 0:
    print("This number is even!")
    if number % 4 == 0:
        print("This number also accepts division on 4!")
else:
    print("This number is odd!")

num = int(input("Enter the first number: "))
check = int(input("Enter the second number: "))
if check % num == 0:
    print("The first number divides evenly into the second one!")
else:
    print("The first number doesn't divide evenly into the seond one!")