#Tue Jul 28, 2026

#Variable Switch
a = int(input("a = "))
b = int(input("b = "))

a, b = b, a

print(f"a is {a} and b is {b} .")

#Triangular number calculator

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "numbers is:", total)

#Factorial Calculator 

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "is:", factorial)


#Count Digits

number = abs(int(input("Enter a number: ")))

count = 0

if number == 0:
  count = 1
else:
  while number > 0:
    count += 1
    number //= 10
print("Digits:", count)
