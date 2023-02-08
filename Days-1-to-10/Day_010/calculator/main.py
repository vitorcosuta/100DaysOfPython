from os import name, system
from art import logo

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def add(number_1, number_2):
    """Adds a number to another number. Returns the sum of two given numbers."""
    return number_1 + number_2

def subtract(number_1, number_2):
    """Subtracts the second number from the first number. Returns the difference of two given numbers."""
    return number_1 - number_2

def multiply(number_1, number_2):
    """Multiplies a number by another number. Returns the product of the two given numbers."""
    return number_1 * number_2

def divide(number_1, number_2):
    """Divides the first number by the second number. Returns the decimal quocient from the division of the two given numbers."""
    return number_1 / number_2

def is_valid_operation(symbol):
    """Verifies whether the given symbol is a valid operation or not."""
    if symbol == "+" or symbol == "-" or symbol == "*" or symbol == "/":
        return True
    return False

def print_operations():
    """Prints the symbols of the basic operations and the name of their respective operations."""
    for symbol in operations:
        string1 = f"\n{symbol} : "
        
        if symbol == "+":
            string1 += "Add"
        if symbol == "-":
            string1 += "Subtract"
        if symbol == "*":
            string1 += "Multiply"
        if symbol == "/":
            string1 += "Divide"
            
        print(string1)

def is_valid_answer(answer):
    if answer == 'yes' or answer == 'no':
        return True
    return False    

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():

    print(logo + "\n\n")
    should_continue = True
    previous_result = float(input("What's the first number?  "))
    
    while should_continue:
    
        print_operations()
    
        operation_symbol = input("\nPick an operation from the symbols above: ")
        
        while not is_valid_operation(operation_symbol):
            print("That's not a valid operation.")
            operation_symbol = input("\nPick an operation from the symbols above: ")
    
        next_number = float(input("\nWhat's the next number?  "))
    
        # Notice how we can here assign a function to a key in a dictionary and call this same function by the means of another variable
        calculation = operations[operation_symbol] # Points to a memory address that points to a function
        result = calculation(previous_result, next_number) # Points to a numeric (int) value
        print(f"\n{previous_result} {operation_symbol} {next_number} = {result}")
        previous_result = result
    
        answer = input("\nDo you want to start a new calculation? \"Yes\" or \"No\"?  ").lower()
        
        while not is_valid_answer(answer):
            print("That's not a valid answer.")
            answer = input("\nDo you want to start a new calculation? \"Yes\" or \"No\"?  ").lower()
    
        if answer == 'yes':
            should_continue = False
            clear()
            calculator()

calculator()