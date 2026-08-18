#Sat Aug 15, 2026

for i in range(len(a)):
    for j in range(i + 1, len(a)):
         if a[i] + a[j] == 12:
           print(f"We found a valid pair: {a[i]} + {a[j]}")


count = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
         if a[i] + a[j] == 12:
           count += 1

print(count)
