num = int(input('Enter a number: '))    # Taking Input
rev = 0
num2 = num      # To avoid changing input value
while num2 != 0:    # Using num2 in the process
    rem = num2 % 10
    rev = rev * 10 + rem
    num2 //= 10
if num == rev:      # Checking the codition
    print(f'The number {num} is a palindrome.')
else:
    print(f'The number {num} is not a palindrome.')
