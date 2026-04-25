from art import logo

# Operation Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1 , n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

# Dictionary of operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Main calculator function
def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = result
        else:
            should_continue = False
            calculator()  # Recursively restart calculator

# Run the calculator
calculator()
