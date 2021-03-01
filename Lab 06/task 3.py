num = int(input('Enter a single digit odd number: '))   # Taking Input
if 0 < num < 10 and (num % 2) != 0:     # Applying Single Digit Odd Number Condition
    i = 1
    while i <= num:     # Printing The First Line
        print(f'{num}', end=' ')
        i += 1
    print()     # Moving to the next line
    j = 1       # as line number after the first line
    num2 = num    # to avoid changing num in process
    num2 -= 2
    k = num - 4     # To control number of spaces
    while j <= (num//2):
        print('  '*j, f'{num2} ', '  '*k, sep='', end='')
        if j != (num//2):    # To avoid having '1' two times in the last line
            print(f'{num2}')
        num2 -= 2
        j += 1
        k -= 2
else:
    print('Invalid Input... (Single digit odd numbers only)')
