def addition(first_num, sec_num):       #Defining functions for each operation
    add = first_num + sec_num
    return add
def subtraction(first_num, sec_num):
    sub = first_num - sec_num
    return sub
def multiplication(first_num, sec_num):
    multi = first_num * sec_num
    return multi
def division(first_num, sec_num):
    div = first_num / sec_num
    return div
def remainder(first_num, sec_num):
    rem = first_num % sec_num
    return rem
def exponent(first_num, sec_num):
    exp = first_num ** sec_num
    return exp
def show_message():     # Defining function to show the main message
    print(f'First Number = {first_num}, Second Number = {sec_num}')
    print('n - Enter new numbers\n')
    print('a - Addition')
    print('s - Subtraction')
    print('m - Multiplication')
    print('d - Division')
    print('r - Remainder')
    print('e - Exponentiation\n')
    print('x - Exit program')
    num = input('Select an option: ')
    return num
def display_output(num):        # Defining function for displaying output
    if num == 'a':
        add = addition(first_num, sec_num)
        print(f'Sum of {first_num} & {sec_num}: {add}')
    elif num == 's':
        sub = subtraction(first_num, sec_num)
        print(f'Difference of {first_num} & {sec_num}: {sub}')
    elif num == 'm':
        multi = multiplication(first_num, sec_num)
        print(f'Product of {first_num} & {sec_num}: {multi}')
    elif num == 'd':
        div = division(first_num, sec_num)
        print(f'Quotient of {first_num} & {sec_num}: {div}')
    elif num == 'r':
        rem = remainder(first_num, sec_num)
        print(f'Remainder of {first_num} & {sec_num}: {rem}')
    elif num == 'e':
        exp = exponent(first_num, sec_num)
        print(f'{first_num} with exponent {sec_num}: {exp}')
    else:
        pass
    print()
first_num = None    # As specified in the question
sec_num = None
num = show_message()    # Taking command letter
while num != 'x':
    if num != 'a' and num != 's' and num != 'm' and num != 'd' and num!= 'r' and num != 'e' and num != 'n':
        print('Invalid Input... Try entering letters mentioned above.\n')
        break       # In case of invalid input
    first_num = int(input('Enter first number: '))  # Taking values
    sec_num = int(input('Enter second number: '))
    print()     # Spaces for better outlook
    num = show_message()    # Taking command letter
    display_output(num)     # Displaying output
else:
    print('Program exited successfully.')   # Exit message
