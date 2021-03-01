l = 0     # l is to reduce the number of asterisks with every line
for i in range(5):
    for k in range(i):      # k depends on i to increment its value with every line
        print(' \t', end='')
    for j in range(9-l):    # j depends on l to decrement its value with every line
        print('*\t', end='')
    print('\n')     # Moving to next line
    l += 2      # Since Asterisk decrease by 2 with every line
