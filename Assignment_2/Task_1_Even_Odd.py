'''
Task 1: Check if a Number is Even or Odd
Problem Statement:  Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly. '''

# Expected output
#Enter a number: 7
#7 is a odd number.


a = int(input('Enter a Number: '))
if ((a % 2) == 0):
    print(a ,"is a Even number.")
else:
    print(a , "is an odd number.")
