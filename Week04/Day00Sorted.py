#Sun Aug 8, 2026

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

sortednums = sorted(nums)

print(sortednums)
print(nums)

# Practice

# Write programs that:

# Sort a list without keeping the original.
# Sort a list while keeping the original.
# Find the smallest number using sorting.
# Find the largest number using sorting.

nums = [1,3,5,4,2]

good = nums.sort()

print(nums)

#
nums = [1,3,5,4,2]

better = sorted(nums)

print(nums)
print(better)

#
nums = [1,3,5,4,2]

great = sorted(nums)
print(great[0])

#
nums = [1,3,5,4,2]

greatest = sorted(nums)
print(greatest[-1])
