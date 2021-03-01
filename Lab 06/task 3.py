def mil_km(num1):
    '''mil_km(x)
        Returns x in kilometer'''
    km = num1 * 1.609
    return km
def cel_fahren(num1):       # Defining functions seperately
    '''cel_fahren(x)
        Returns x in Fahrenheit'''
    fahren = ((1.8) * num1) + 32
    return fahren
def ft_mtr(num1):
    '''ft_mtr(x)
        Returns x in meters'''
    mtr = num1 * 0.3048
    return mtr
def yrd_mtr(num1):
    '''yrd_mtr(x)
        Returns x in meters'''
    mtr = num1 * 0.9144
    return mtr
inp = 'a'   # Defining variable to enter in the loop
while inp != 'e':
    print('Which conversion do you want to do?\n\nEnter (a) for miles to km.')
    print('Enter (b) for Celsius to Fahrenheit.\nEnter (c) for feet to meters.')
    print('Enter (d) for yards to meters.\nEnter (e) to exit a program.\n')
    inp = input('Enter here: ')     # Taking Input
    if inp == 'a':
        mil = float(input('Enter miles: '))
        km = mil_km(mil)
        print(f'{mil} miles = {km} kilometer\n')
    elif inp == 'b':
        cel = float(input('Enter Celsius: '))
        fahren = cel_fahren(cel)
        print(f'{cel} celsius = {fahren} fahrenheit\n')
    elif inp == 'c':        # Calling different function for each input value
        ft = float(input('Enter feet: '))
        mtr = ft_mtr(ft)
        print(f'{ft} feet = {mtr} meters\n')
    elif inp == 'd':
        yrd = float(input('Enter yards: '))
        mtr = yrd_mtr(yrd)
        print(f'{yrd} yards = {mtr} meters\n')
    elif inp == 'e':
        continue
    else:
        print('Invalid Input... Try entering the letters mentioned above.\n')
else:
        print('Program exited successfully.')
