print("hello")


def factorial(n):
    """
    Calculate the factorial of a number using recursion.
    :param n: Non-negative integer
    :return: Factorial of n
    """
    if n == 0 or n == 1:  # Base case
        return 1
    else:  # Recursive case
        return n * factorial(n - 1)

# Example usage
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {number} is {factorial(number)}.")
