#Thu Aug 13, 2026

numbers = [2, 3, 5, 6, 8]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])

