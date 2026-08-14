#Wed Aug 12, 2026

numbers = [8, 3, 7, 2, 9]

numbers.sort()

best = float("inf")

for i in range(len(numbers) - 1):
    gap = numbers[i + 1] - numbers[i]
    best = min(best, gap)

print(best)
