c=float(input('Enter the First Number:'))
b=float(input('Enter the Second Number:'))
o=input('Enter the Arithmetic Operation:')
if o=='+':
    print(c+b)
elif o=='-':
    print(c-b)
elif o=='*':
    print(c*b)
elif o=='/':
    print(c/b)
else:
    print('Not Supported')