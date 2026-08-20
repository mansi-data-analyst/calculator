Python Terminal Calculator
Learning Assignment
Your task is to create a calculator program using Python that runs directly in the terminal. The goal is to practice functions, user input, conditional statements, loops, and error handling.
1. Learning Objectives
•	Create and use Python functions.
•	Take input from the user using input().
•	Convert user input into numbers.
•	Use if/elif/else statements.
•	Use a while loop to keep the calculator running.
•	Handle common errors such as division by zero and invalid input.
•	Write clean, readable, and structured Python code.
2. Required Calculator Operations
Create separate functions for each operation:
•	Addition
•	Subtraction
•	Multiplication
•	Division
•	Modulus (remainder)
•	Power / Exponent
3. Suggested Function Structure
Use a separate function for every mathematical operation. For example:
def add(num1, num2):
    # return the sum
    pass
Create similar functions for subtraction, multiplication, division, modulus, and power.
4. Terminal Menu
When the program starts, show a menu similar to this:
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
5. Program Flow
1.	Display the calculator menu.
2.	Ask the user to select an operation.
3.	If the user selects Exit, stop the program.
4.	Ask the user to enter two numbers.
5.	Call the correct function based on the selected operation.
6.	Display the result clearly.
7.	Ask whether the user wants to perform another calculation.
8.	Continue until the user chooses to exit.
6. Important Error Handling
•	Do not allow division by zero.
•	Do not allow modulus by zero.
•	Handle invalid number input using try/except.
•	Handle invalid menu choices gracefully.
7. Expected Example
Enter your choice (1-7): 3
Enter first number: 10
Enter second number: 5

Result: 10.0 * 5.0 = 50.0

Do you want to calculate again? (yes/no): yes
8. Bonus Challenge
•	Add square root functionality.
•	Allow calculation history.
•	Allow the user to clear the history.
•	Format the output professionally.
•	Organize the program into reusable functions.

Submission: Create one Python file named calculator.py and make sure it can run from the terminal using:
python calculator.py
