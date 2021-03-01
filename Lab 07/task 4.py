def next_prime(num):    # Function to return next prime number.
    '''next_prime(x)
        Returns smallest prime number after x.'''   # Documentation
    def is_prime(num):      # Function to chech if input is a prime.
        '''is_prime(x)
            Checks if x is a prime or not.'''    # Documentation
        if num > 1:
            for i in range(2, num):
                if num % i == 0:    # Divide by increasing numbers until factor is found.
                    print(f'{num} is not a prime number.\n')
                    break
            else:   # If factor's found, else: won't be printed.
                print(f'{num} is a prime number.\n')
        else:       # 1 & lower numbers are not prime.
            print(f'{num} is not a prime number.\n')
    is_prime(num)   # Calling func. to check the input.
    nxt_prime = num + 1
    prime = None    # To enter the while loop.
    while prime != True:    # prime equals True when prime number is found.
        if nxt_prime > 1:
            for i in range(2, nxt_prime):
                if nxt_prime % i == 0:
                    prime = False
                    break   # If no factor found, else: will be printed.
            else:
                prime = True
                return nxt_prime
        else:   # 1 & lower numbers are not prime.
            prime = False
        nxt_prime += 1
num = None      # To enter while loop
while num != str():
    num = input('Enter an integer: ')   # Taking input.
    if num.isdigit() == True:       # if num is digit, then running the whole program.
        num = int(num)
        nxt_prime = next_prime(num)     # Calling func. to find next prime.
        print(f'Next prime number: {nxt_prime}\n')
    else:   # If num is not a positive digit.
        print('Invalid Input... (Negative Integers / String Value)')
        print('Program exited successfully.')
        break
