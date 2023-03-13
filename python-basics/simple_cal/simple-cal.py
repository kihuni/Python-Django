num1 = int(input('Enter firsts number: ')) # gets user first number
num2 = int(input('Enter second number: ')) # gets user second number
op = input('Enter Operator: ') 

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
elif op == '%':
    print(num1%num2)
else:
    print('Invalid operator!')