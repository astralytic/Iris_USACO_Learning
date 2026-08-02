#Sun Aug 2, 2026

Favorites = []

month = input("What is your favorite month? ").capitalize()
season = input("What is your favorite season? ").capitalize()

Favorites.append(month)
Favorites.append(season)

print("Your favorite month is: " + Favorites[0])
print("Your favorite season is: " + Favorites[1])

#Next Version
Month = input("What is your favorite month? ").capitalize()

if "Dec" in Month or "Jan" in Month or "Feb" in Month:
    print("Your favorite month is in: Winter")
elif "Mar" in Month or "Apr" in Month or "May" in Month:
    print("Your favorite month is in: Spring")
elif "Jun" in Month or "Jul" in Month or "Aug" in Month:
    print("Your favorite month is in: Summer")
elif "Sep" in Month or "Oct" in Month or "Nov" in Month:
    print("Your favorite month is in: Fall")
else:
    print("That is not a valid month.")

#.pop()
nums = [1, 2, 3, 4, 5]

x = nums.pop()

print(x)
print(nums)

#Next Version
import random

nums = [1, 2, 3, 4, 5]

randindex = random.randrange(len(nums))
x = nums.pop(randindex)

print(x)
print(nums)

#Even Better
import random

start = int(input("Start number: "))
end = int(input("End number: "))

nums = list(range(start, end + 1))

random_index = random.randrange(len(nums))
x = nums.pop(random_index)

print(x)
print(nums)
