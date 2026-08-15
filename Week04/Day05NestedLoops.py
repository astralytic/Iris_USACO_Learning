#Fri Aug 14, 2026

#This is wrong: 

i = 3

for x in range(1, i + 2):
    for j in range(1, i + 2):
        print(x, j)

#because it prints out duplicates.

#I want:

numbers = [1, 2, 3, 4]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])

#Next

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
best = 0

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]
        best = max(best, product)

print(best)
