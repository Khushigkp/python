# For numbers 1 to 12, create a dictionary where:
# If the number is divisible by 3 → value = number cubed
# If divisible by 4 (but not 3) → value = number squared
import math;

dec = {
    num: (num**3 if num % 3 == 0 else num**2) 
    for num in range(1, 13) 
    if num % 3 == 0 or num % 4 == 0
}
print(dec)

