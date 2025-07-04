
def perform_operation(num1: float, num2: float, operation: str):
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                print("Error: cannot divide by zero")
                return None
            else:
                return num1 / num2
        case _:
            print("Invalid operation. Please choose from +, -, *, /")
            return None
    