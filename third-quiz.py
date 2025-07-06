llist = []
newlist = []
length = int(input("Enter the length of the list: "))
for i in range(length):
    x = int(input("Enter an element: "))
    llist.append(x)
    if x < 5:
        print(x)
        newlist.append(x)
print(newlist)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
ref = int(input("Enter the number: "))
for i in range(len(a)):
    if a[i] < ref:
        b.append(a[i])
print(b)