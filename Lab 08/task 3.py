import MaxMin       # Importing module for task (b)
import AscendSort as AscSort    #Importing module for task (d)
input_list = list()
inp = str()      # To enter while loop
while inp != 'E':
    print('Enter N to enter the numbers again.')
    print('Enter M for max. & min. numbers in this list.')
    print('Enter S for sum of squares of each number in this list.')
    print('Enter A for sorting this list in ascending order.')
    print('Enter E to exit the program.')
    inp = input('\nEnter you choice here: ')    # Taking input
    if inp == 'N':
        input_list = list()     # Emptying the previous values from this list
        print('\nEnter X to stop entering numbers.\n')
        num = input('Enter a number: ')     # Taking Input
        while num != 'X':
            num = int(num)      #Typecasting string into integers
            input_list.append(num)
            num = input('Enter next number: ')
        print('\nA list of numbers is ready!\n')
        continue
    elif inp == 'M':
        max_num, min_num = MaxMin.maxmin(input_list)    # Using MaxMin Module
        print(f'\nMaximum number of this list: {max_num}')
        print(f'Minimum number of this list: {min_num}\n')
    elif inp == 'S':
        output_list = map(lambda x : x ** 2, input_list)
        output = 0
        for nums in output_list:
            output += nums      # Adding all the squares into output
        print(f'\nSum of Squares of each number in this list: {output}\n')
    elif inp == 'A':
        output_list = AscSort.ascend_sort(input_list)       # Using AscSort module
        print('\nThe list in Ascending order: ', end='')
        print(output_list, end='\n\n')
    elif inp == 'E':
        break
    else:       #In case of invalid character
        print('\nInvalid Input... Try entering the letters mentioned above.\n')
print('\nProgram exited successfully.')     # Exiting message
