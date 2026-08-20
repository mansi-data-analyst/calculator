# Python Terminal Calculator
# create Func -> add, sub, mul, div, 
# user Inputs -> (1-7)
# error Handling 

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def mod(num1, num2):
    return num1 % num2

def power(num1, num2):
    return num1 ** num2

# user Inputs
def user_input():
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        return num1, num2

def main():
    print("""
    ==============================
          PYTHON CALCULATOR
    ==============================
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Modulus
    6. Power
    7. Exit
    ==============================
    """)
    
    # while true -> infinite loop
    while True:
        choice = input("Enter your choice (1-7): ")
        if choice == "7": # exit condition
            break # exit this loop
        num1, num2 = user_input() # get user input
        if choice == "1":
            print("Result: ", add(num1, num2))
        elif choice == "2":
            print("Result: ", sub(num1, num2))
        elif choice == "3":
            print("Result: ", mul(num1, num2))
        elif choice == "4":
            print("Result: ", div(num1, num2))
        elif choice == "5":
            print("Result: ", mod(num1, num2))
        elif choice == "6":
            print("Result: ", power(num1, num2))
        else:
            print("Invalid choice. Please try again.")

main()


