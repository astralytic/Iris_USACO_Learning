#Sun Aug 16, 2026

a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
          print(a[i], a[j], a[k])


best = 0
a = [1, 2, 3, 4, 5]
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for k in range(j + 1, len(a)):
          if a[i] + a[j] + a[k] > best:
            best = a[i] + a[j] + a[k]

print(best)
