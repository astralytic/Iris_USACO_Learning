#Mon Aug 3, 2026


while True:
    expr = input("\nEnter calculation (e.g. 5. + 3, 4 ** 2, 10 / 2) or 'exit' to quit: ")
    if expr.lower() == 'exit':
        break
    try:
        num1, op, num2 = expr.split()
        n1, n2 = float(num1), float(num2)

        if op == '+':
            print(f"Result: {n1 + n2}")

        elif op == '-':
            print(f"Result: {n1 - n2}")

        elif op == '*':
            print(f"Result: {n1 * n2}")

        elif op == '/':
            if n2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {n1 / n2}")

        elif op == '**':
            print(f"Result: {n1 ** n2}")

        else:
            print("Error: Unsupported operator. Please use +, -, *, /, or **.")

    except ValueError:
        print("Error: Invalid input format. Please use spaces between numbers and operator (e.g. 5 + 3).")
