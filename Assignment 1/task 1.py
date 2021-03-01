num = int(input('Enter a natural number: '))    # Taking Input
num1, num2 = 0, 1
if num > 1:     # If N is greater than 1
    print(f'{num} first Fibonacci Series numbers are as follows:\n')
    print(f'{num2}', end=', ')
    for i in range(1, num):
        fibonacci = num1 + num2     # Addition of two preceding numbers
        print(f'{fibonacci}', end=', ')
        num1 = num2
        num2 = fibonacci    # Replacing values for the next loop
    print('...')
elif num == 1:      # If N is 1
    print(f'{num2}')
else:       # If N is not a natural number
    print('Invalid Input...(Natural numbers only)')
