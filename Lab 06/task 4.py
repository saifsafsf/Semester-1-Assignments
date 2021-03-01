def factorial(rem):
    '''factorial(x)
        Returns factorial of x.'''  # Documentation
    factorial = 1
    for i in range(1, rem+1):
        factorial *= i      # Calculating factorial
    return factorial
yesquit = 'y'   # To enter in while loop
while yesquit == 'y':
    num = int(input('Enter a number: '))    # Taking Input
    result = 0
    num1 = num      # To avoid changing input value
    while num1 != 0:    # Using num1 in the process
        rem = num1 % 10
        factorial1 = factorial(rem)     # Calling function
        result += factorial1
        num1 //= 10     # Changing value
    if result == num:   # Displaying Output
        print(f'{num} is a strong number.\n')
    else:
        print(f'{num} is not a strong number.\n')
    yesquit = input('Enter (y) to continue or (q) to quit: \n')
    if yesquit == 'q':
        print('Programm exited successfully.')
    elif yesquit != 'y':
        print('Invalid Input... You did not enter (y) or (q)')


