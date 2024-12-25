import os


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operators_dict = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    number_1 = float(input('Enter First Number: '))
    for i in operators_dict:
        print(i)

    continue_flag = True
    while continue_flag:
        op_symbol = input('Pick an operator: ')
        number_2 = float(input('Enter Next Number: '))
        calculator_function = operators_dict[op_symbol]
        output = calculator_function(number_1, number_2)
        print(f'{number_1} {op_symbol} {number_2} = {output}')

        should_continue = input(f"enter 'y' to continue calculation with {output} or 'n' to start a new calculation "
                                f"or 'x' to exit: \n").lower()
        if should_continue == 'y':
            number_1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag = False
            print('Bye, have a nice day!')


calculator()

#add = add(number_1,number_2)
#subtract = subtract(number_1, number_2)
#multiply = multiply(number_1, number_2)
#divide = divide(number_1, number_2)
