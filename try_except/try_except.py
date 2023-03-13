try:  
    num1 = input('Enter first number: ')
    num2 = int(input('Enter second number'))
    op = input('Enter operetor: ')

    if op == '+':
        print( 'Equal to ' + num1 + num2)
except:
    print('Something Went Wrong, Try again')
else:
    print('Nothing Went Wrong ')
finally:
    print('I run regardless of the result of the try- and except blocks')