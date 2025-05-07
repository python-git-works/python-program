''' Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum. '''

# Expected output
# The sum of number from 1 to 50 is:

# Using range function
'''n = list(range(1,51))
print(sum(n)) '''

# Using for loop
total = 0

for i in range(1,51):
    total += i
print("The sum of numbers from 1 to 50 is:", total)