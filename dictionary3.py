# Create a dictionary for numbers 1 to 10 such that:
# Only even numbers are included as keys
# The value should be the factorial of that number
import math
even_factorials = {num: math.factorial(num) for num in range(1, 11) if num % 2 == 0}
print(even_factorials)
