active = True
while active:

    num1 = int(input('Enter first number: '))
    oper = input('Enter operations: ')
    num2 = int(input('Enter second number: '))
    #dict_ = {'+': 'num1 + num2', '-': 'num1 - num2', '*': 'num1 * num2', '/': 'num1 / num2'}
    if oper  == '+':
        print(num1+num2)
    elif oper == '-':
        print(num1-num2)
    else:
        if oper == '*':
            print(num1*num2)
        elif oper == '/':
            try:
                num1 / num2 == 0
            except ZeroDivisionError:
                print('Division by zero is forbidden!')
            else:
                print(num1/num2)
        else:
            print('Wrong operations')
    
    continue_ = input('If you want continue click any button and Enter, if not click to Enter: ')
        