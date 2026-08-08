#Fri Aug 7, 2026


alice = int(input("Enter Alice's score: "))
bob = int(input("Enter Bob's score: "))
charlie = int(input("Enter Charlie's score: "))

scores = {
    "Alice": alice,
    "Bob": bob,
    "Charlie": charlie,
}

for score in scores:
    print(scores.get(score)) 



nums = [3, 5, 7, 9, 11, 5, 3, 7, 9, 11, 5, 3]

count = {}

for num in nums:
    if num not in count:
        count[num] = 0
    count[num] += 1

print(count)



nums = list(map(abs, map(int, input("Enter numbers separated by spaces: ").split())))

print(nums)
