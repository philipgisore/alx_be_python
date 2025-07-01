try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose the operation (+, -, *, /):")

    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num1 != 0:
                result = num1 / num2
                print(f"The result is {result}")
            else:
                print("Error: Division by zero is not allowed")

except ValueError:
    print("Invalid input. Please enter numeric values.")