#Sat Aug 8, 2026

#
seen = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
x = int(input("Enter a number to check if it's in the set: "))

print(seen)
print(len(seen))
print(type(seen))
print(x in seen)

if x in seen:
    print(f"{x} is in the set.")
else:
    print(f"{x} is not in the set.")
#
Convert input to a set to remove duplicates, then to a list to sort
nums = sorted(list(set(int(x) for x in input("Enter some numbers separated by spaces: ").split())))

print(nums)
#
import random

# 1. List containing 5 random numbers
list_5 = [random.randint(1, 100) for _ in range(5)]
print("Original 5 random numbers:", list_5)
list_5.sort()
print("Sorted 5 random numbers:", list_5, "\n")

# 2. List containing 10 random numbers
list_10 = [random.randint(1, 100) for _ in range(10)]
print("Original 10 random numbers:", list_10)
list_10.sort()
print("Sorted 10 random numbers:", list_10, "\n")

# 3. List containing negative and positive numbers
list_mixed = [random.randint(-50, 50) for _ in range(8)]
print("Original mixed (negative and positive):", list_mixed)
list_mixed.sort()
print("Sorted mixed:", list_mixed, "\n")

# 4. List containing repeated numbers
# (Using a small range like 1 to 5 ensures duplicates are generated)
list_repeated = [random.randint(1, 5) for _ in range(8)]
print("Original with repeated numbers:", list_repeated)
list_repeated.sort()
print("Sorted repeated numbers:", list_repeated)
