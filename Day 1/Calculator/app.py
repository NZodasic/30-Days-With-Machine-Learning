# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        # Take input from the user
        choice = input("Enter choice(1/2/3/4): ")

        # Check if the input is one of the four options
        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        
        # Option to exit the loop
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes' and next_calculation.lower() != 'y':
            break

    print("Exiting Calculator. Goodbye!")

# Call the calculator function
calculator()
