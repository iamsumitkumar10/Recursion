
print("test case")


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

# Fixed number for factorial calculation
number = 5  # You can change this value as needed
result = factorial(number)
print(f"The factorial of {number} is {result}.")
