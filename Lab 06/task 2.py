print('Program to sum up any ten even numbers.\n')
print('Enter 10 even numbers:')
rem_nums = 10   # variable counting number of remaining numbers
sum_nums = 0
while rem_nums > 0:
    num = int(input(f'Remaining Numbers: {rem_nums}, Enter an even number: '))
    if (num % 2) != 0:  # Applying condition
        print(f'{num} is not an even number. Try entering an even number.\n')
        continue
    sum_nums += num
    rem_nums -= 1
print(f'\nThe sum of 10 even numbers: {sum_nums}')
