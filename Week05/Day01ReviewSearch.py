#Mon Aug 17, 2026

a = [4, 8, 2, 9, 1]
best = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x = a[i] + a[j]
        if x > best:
          best = x
print(best)

#Changed it to become largest difference.
a = [3, 8, 2, 10, 5]
best = 0

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        x = a[j] - a[i]
        if x > best:
          best = x
print(best)


