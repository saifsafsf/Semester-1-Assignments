num = int(input('Enter a natural number: '))    # Taking input
if num > 0:
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i      # Calculating factorial
    print(f'The factorial of {num} = {factorial}')
else:
    print('Invalid Input... (Natural numbers only)')
