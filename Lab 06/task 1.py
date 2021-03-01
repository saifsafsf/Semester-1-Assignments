a = 20   # Given values
while a >= 0:
    b = 5
    while b >= 0:
        print(end = f'({a}, {b})')  # Using end= not to move to next line
        if b > 0:
            print(end = '\t')
            b -= 1
            continue
        b -= 1

    print()     # Now moving to next line
    a -= 1
