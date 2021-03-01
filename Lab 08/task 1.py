math_exp = input('Enter a mathematical expression: ')   # Taking Input
while math_exp != 'Quit':
    math_exp = eval(math_exp)   # Evaluating Input
    print(f'Result of the expression: {math_exp:.3}\n')
    print('Enter Quit to exit the program OR')      # Taking input for next iteration
    math_exp = input('Enter another mathematical expression: ')
print('Program exited successfully.')   # Exiting message
