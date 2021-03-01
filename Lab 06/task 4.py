num = int(input('Enter a number: '))    # Taking Input
rev = 0
num2 = num      # To avoid changing input value
while num2 != 0:    # Using num2 in the process
    rem = num2 % 10
    rev = rev * 10 + rem
    num2 //= 10
print(f'The reverse of {num} is {rev}')
