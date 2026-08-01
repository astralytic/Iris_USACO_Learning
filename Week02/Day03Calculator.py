#Wed Jul 29, 2026

#Calculator

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def format_list(numbers):
    if len(numbers) == 0:
        return "There is no number"
    elif len(numbers) == 1:
        return f"{numbers[0]}"
    elif len(numbers) == 2:
        return f"{numbers[0]} and {numbers[1]}"
    else:
        all_but_last = ", ".join(str(n) for n in numbers[:-1])
        return f"{all_but_last}, and {numbers[-1]}"

numbers = []
print("Welcome to The Math Corp. Forever Adder. Press Enter with no number to stop.")


while(True):
    entry = input(f"Enter Number #{len(numbers) + 1} (Optional): ")
    if entry == "":
        break
    numbers.append(float(entry))

if len(numbers) == 1:
    print(f"{format_list(numbers)} is obviously equal to {sum_list(numbers)}! The Math Corp. does not thank you for your use.")
elif len(numbers) == 0:
    print(f"{format_list(numbers)} so you are not supposed to use this tool! The Math Corp. does not thank you for your use.")
else:
    print(f"The sum of {format_list(numbers)} is {sum_list(numbers)}! The Math Corp. thanks you for your use.")
