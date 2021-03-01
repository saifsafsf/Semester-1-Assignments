num = int(input('Enter a natural number: '))    # Taking input
if num > 0:
    print(f'The multiplication table of {num}:')
    for i in range(1, 11):      # Displaying output
        print(f'{num} X {i} = {num*i}')
else:
    print('Invalid Input... (Natural numbers only)')
