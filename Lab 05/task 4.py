star = str('*')     # Specifying variables
for i in range(1, 14):
    print(f'{i}\t', end='')    # Using end= so cursor stays in the same line
    for j in range(1, i+1):
        print(star, end='')     
    print()     # Now moving to next line for the next line of output
