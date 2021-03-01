num = int(input('Enter a natural number: '))    # Taking input
sum = 0
if num >= 1:    # Applying condition
    for i in range(1, num+1):
        sum += i    # Adding the numbers into the "sum"
    print(f'Sum of the numbers 1 to {num}: {sum}')
else:
    print('Invaid input... (Natural Numbers only)')
