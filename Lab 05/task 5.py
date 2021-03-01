num = int(input('Enter number of rows: '))      # Taking Input
if num > 0:
    for i in range(1, num+1):
        for j in range(num-i):   # Displaying Spaces
            print(end=' ')
        for k in range(i):     # Displaying Asterisks
            print('*', end=' ')
        print()

# ESEs Prep.

    for i in range(1, num+1):
        print(end = ' \t'*(num-i))
        for j in range(1, i+1):
            print(end = str(j))
            if j < i:
                print(end = '\t')
                continue
            print()

# ESEs Prep.

else:
    print('Invalid Input... (Natural numbers only)')

