'''
#celcius -----> Fahrenheit

c=input('Celcius :')
c= float(c)
f=(c * 9/5) +32
print('Fahrenheit: ',f)


# Fahrenheit ---> celcius

f=input('Fahrenheit:')
f=float(f)
c=(f - 32) * 5/9
c=int(c)
print('Celcius: ',c)
'''


# SI CALCULATOR

#Eqn = Pnr/100

p=input('P: ')
n=input('n: ')
r=input('r: ')
p=int(p)
n=int(n)
r=int(r)

si=(p*r*n)/100
print('Simple Interest is:',si)