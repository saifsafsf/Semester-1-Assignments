def check_disarium(num2, num, result, exp):     # Defining Function
    '''check_disarium(input, input, output, exponent)
        Returns if input is a Disarium or not.'''   # Documentation
    while num2 != 0:
        rem = num2 % 10
        result += rem ** exp    # Adding each digit with its position in exponent
        exp -= 1     # Decrementing exponent after each cycle
        num2 //= 10     # Decrementing value for next iteration

    return result

num = 0
result = None

while num != result:
    num = int(input('Enter a natural number: '))    # Taking input
    if num > 0:
        num2 = num      # To avoid changing the value in 'num'
        result = 0
        exp = len(str(num))     # length of the number entered
        result = check_disarium(num2, num, result, exp)
        if num == result:   # As specified in the question
            print(f'{num} is a disarium number.\n')
            print('Program exited successfully.')
            break
        print(f'{num} is not a disarium number.\n')

    else:   # Natural numbers only
        print('Invalid Input... Please enter a natural number only.\n')
