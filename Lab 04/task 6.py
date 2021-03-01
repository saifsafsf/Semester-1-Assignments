num = int(input('Enter a natural number: '))    # Taking Input
if num > 0:
    for i in range(1, num+1):
        for j in range(num-i):
            print(' \t', end='')    # Printing Spaces
        for k in range(1, 1+i):
            print(f'{k}\t', end='') # Printing Numbers
        print()
else:
    print('Invalid Input... (Natural numbners only)')
