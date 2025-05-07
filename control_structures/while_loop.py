# a---> 5 times using while loop

# counter Variable --> Using counter variable we can specify the test expression.
#while (test expression):
    #statement
    #Increment / Decrement

#Using Increment
'''
counter =1
while  counter <=5:
    print('a')
    counter = counter +1

#Using Decrement
# this will go in infinite loop
counter =1
while  counter <=5:
    print('a')
    counter = counter - 1

# Decrement updated code

counter =5
while  counter >=1:
    print('apple')
    counter = counter - 1

count = 0
while (count <=10):
    print(count)
    count = count + 1 '''

# This code will go in infinite loop.. Variable name mismatch
''' counter = 1
while (counter<=5):
    print("Python")
    count = counter + 1 '''

# Corrected Code
counter = 1
while (counter<=5):
    print("Python")
    counter = counter + 1



