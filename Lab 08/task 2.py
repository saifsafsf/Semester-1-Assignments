import Areas    # Importing module
def area_cyl(radius, height):       # Documentation
    '''area_cyl(radius, height)
        Returns area of corresponding cylinder'''   
    cyl_area = 2 * 3.1416 * radius * (height + radius)     # Usig formula
    return cyl_area
inp = None      # To enter the loop
while inp != 'Quit':
    print('Enter T for Triangle\'s Area.')
    print('Enter C for Circle\'s Area')
    print('Enter R for Rectangle\'s Area')
    print('Enter Y for Cylinder\'s Area')
    print('Enter Quit to exit the program')
    inp = input('Enter your choice here: ')
    if inp.lower() == 't':
        base = float(input('\nEnter Triangle\'s base: '))
        height = float(input('Enter Triangle\'s height: '))     # Taking input
        tri_area = Areas.area_tri(base, height)
        print(f'Area of Triangle: {tri_area:.3f}\n')
    elif inp == 'C':
        radius = float(input('\nEnter Circle\'s radius: '))
        cir_area = Areas.area_cir(radius)
        print(f'Area of Circle: {cir_area:.3f}\n')      # Printing output
    elif inp == 'R':
        length = float(input('\nEnter Rectangle\'s length: '))
        width = float(input('Enter Rectangle\'s width: '))
        rec_area = Areas.area_rec(length, width)
        print(f'Area of Rectangle: {rec_area:.3f}\n')
    elif inp == 'Y':
        radius = float(input('\nEnter Cylinder\'s radius: '))
        height = float(input('Enter Cylinder\'s height: '))
        cyl_area = area_cyl(radius, height)
        print(f'Area of Cylinder: {cyl_area:.3f}\n')
    elif inp == 'Quit':
        break
    else:       # In case of invalid inputs.
        print('Invalid Input... Try entering one of the choices given.\n')
print('\nProgram exited successfully.')     # Exiting message




