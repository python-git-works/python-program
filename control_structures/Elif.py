operand_1=int(input('Enter Operand1: '))
operand_2=int(input('Enter Operand2: '))
operator=input('Enter your operator (+,-,*,/): ')

#if (test_expression):
    #statement
#elif (test_expression):
    #statement
#elif....
#else:
    #statment
#statement

if (operator=='+'):
    print(operand_1 + operand_2)
    print("Addition Completed")
elif (operator=='-'):
    print(operand_1 - operand_2)
    print("Substraction Completed")
elif (operator=='*'):
    print(operand_1 * operand_2)
    print("Multiplication Completed")
elif (operator=='/'):
    print(operand_1 / operand_2)
    print("Division Completed")

else:
    print("None")
print("Thank You")
