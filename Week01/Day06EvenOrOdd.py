#Sat Jul 25, 2026

#Weekly Project: Even or Odd
while(True):
    number = input("Enter a number: ")
    if number == "":
        print("Goodbye!")
        break
    try:
        number = int(number)
    except ValueError:
        print("Please enter an integer next time.")
        continue
    if number % 2 == 0:
        print("Your number is even!")
    else:
        print("Your number is odd!")
