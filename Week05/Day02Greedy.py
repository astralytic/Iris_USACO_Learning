#Tue Aug 18, 2026

numbers = [4, 9, 2, 7, 5]

nums = numbers.copy()

biggest = max(nums)
nums.remove(biggest)
less = max(nums)

answer = biggest + less
print(answer)



numbers = [4, 9, 2, 7, 5]

numbers.sort(reverse=True)

choice0 = numbers[0]
choice1 = numbers[1]

print(choice0 + choice1)


numbers = [6, 3, 10, 4, 8]

choice = max(numbers)

print(choice)
