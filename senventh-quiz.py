a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# M1
even = []
for num in a :
    if num % 2 == 0:
        even.append(num)

print(even)

#M2
even = [num for num in a if num % 2 == 0]