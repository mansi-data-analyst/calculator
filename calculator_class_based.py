# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.


class Calculator:
    """
    A class-based calculator that demonstrates basic Object-Oriented Programming (OOP)
    concepts in Python such as classes, objects, instances, variables, and methods.
    """

    def __init__(self):
        """
        Constructor / Initializer method.
        Initializes the state of the Calculator object.
        'self' refers to the specific instance of the class being created.
        """
        self.history = []  # Instance attribute to store calculation history

    def add(self, num1, num2):
        """Adds two numbers, records the operation in history, and returns the result."""
        result = num1 + num2
        self._add_to_history(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        """Subtracts the second number from the first, records it, and returns the result."""
        result = num1 - num2
        self._add_to_history(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        """Multiplies two numbers, records the operation, and returns the result."""
        result = num1 * num2
        self._add_to_history(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        """
        Divides the first number by the second.
        Raises ZeroDivisionError if division by zero is attempted.
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = num1 / num2
        self._add_to_history(f"{num1} / {num2} = {result}")
        return result

    def modulus(self, num1, num2):
        """
        Calculates the remainder of division of num1 by num2.
        Raises ZeroDivisionError if modulus by zero is attempted.
        """
        if num2 == 0:
            raise ZeroDivisionError("Cannot calculate modulus by zero.")
        result = num1 % num2
        self._add_to_history(f"{num1} % {num2} = {result}")
        return result

    def power(self, num1, num2):
        """Calculates num1 raised to the power of num2."""
        result = num1 ** num2
        self._add_to_history(f"{num1} ^ {num2} = {result}")
        return result

    def _add_to_history(self, record):
        """
        A helper method (conceptually private, indicated by leading underscore)
        to append a record to the history list.
        """
        self.history.append(record)

    def get_history(self):
        """Returns the calculation history."""
        return self.history

    def clear_history(self):
        """Clears the calculation history."""
        self.history.clear()


def get_number_input(prompt):
    """Helper function to get and validate numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    # Instantiate the Calculator class
    # 'calc' is an instance/object of the 'Calculator' class
    calc = Calculator()
    while True:
        print("\n" + "=" * 30)
        print("   CLASS-BASED PYTHON CALCULATOR")
        print("=" * 30)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power")
        print("7. View History")
        print("8. Clear History")
        print("9. Exit")
        print("=" * 30)

        choice = input("Enter your choice (1-9): ").strip()

        if choice == "9":
            print("Exiting calculator. Goodbye!")
            break

        if choice == "7":
            history = calc.get_history()
            if not history:
                print("\nHistory is empty.")
            else:
                print("\nCalculation History:")
                for index, record in enumerate(history, 1):
                    print(f"{index}. {record}")
            continue

        if choice == "8":
            calc.clear_history()
            print("\nHistory cleared.")
            continue

        if choice in ["1", "2", "3", "4", "5", "6"]:
            num1 = get_number_input("Enter first number: ")
            num2 = get_number_input("Enter second number: ")

            try:
                if choice == "1":
                    res = calc.add(num1, num2)
                    print(f"\nResult: {num1} + {num2} = {res}")
                elif choice == "2":
                    res = calc.subtract(num1, num2)
                    print(f"\nResult: {num1} - {num2} = {res}")
                elif choice == "3":
                    res = calc.multiply(num1, num2)
                    print(f"\nResult: {num1} * {num2} = {res}")
                elif choice == "4":
                    res = calc.divide(num1, num2)
                    print(f"\nResult: {num1} / {num2} = {res}")
                elif choice == "5":
                    res = calc.modulus(num1, num2)
                    print(f"\nResult: {num1} % {num2} = {res}")
                elif choice == "6":
                    res = calc.power(num1, num2)
                    print(f"\nResult: {num1} ^ {num2} = {res}")
            except ZeroDivisionError as e:
                print(f"\nError: {e}")
        else:
            print("\nInvalid choice. Please choose a number between 1 and 9.")


if __name__ == "__main__":
    main()
