#Thu Jul 30, 2026

#simple for loop
#It has the end function
for i in range(5):
    for n in range(5):
        print(n, end = " ")

#for loop with variables, break, and continue
fruits = ["apple", "banana", "cherry", "avocado"]

for x in fruits:
    if x == "cherry":
        continue
    print(x)
