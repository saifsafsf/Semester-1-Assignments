num = int(input('Enter a number: '))    # Taking Input
numh = num      # Introducing other variables so that num's value doesn't change
numo = num
octal = str()   # Defining data type
octal = '0o'    # The representation of a octal number
hexa = str()
hexa = '0x'     # The representation of a hexadecimal number
hexa1 = str()
octal1 = str()
y = numh // 16      # To have some range, I decided to take this number as range
for i in range(y):
    rem = numh % 16     # Storing the remainder in rem
    if rem == 10:
        hexa1 = 'A' + hexa1
    elif rem == 11:
        hexa1 = 'B' + hexa1
    elif rem == 12:
        hexa1 = 'C' + hexa1
    elif rem == 13:
        hexa1 = 'D' + hexa1
    elif rem == 14:
        hexa1 = 'E' + hexa1
    elif rem == 15:
        hexa1 = 'F' + hexa1
    else:
        hexa1 = str(rem) + hexa1    # hexa1 stores the hexadecimal number with numerous zeroes in the start, i.e. '0x00000153' etc.
    numh //= 16     # numh stores the next number to be divided by 16
for j in hexa1:
    if hexa != '0x':    # This loop works to remove those zeroes in the start
        hexa += j       # j takes each digit and check if it's zero or not. Then, the digit is added to the final answer if needed, and not added if not needed.
        continue
    elif j != '0':
        hexa += j       # The final answer is stored in hexa
    else:
        continue
print(f'The hexadecimal equivalent of {num}: {hexa}')   # To display num here, I avoided changing its value in the process
z = numo // 8   # similiar to y
for k in range(z):
    rem = numo % 8      # storing the remainder in rem
    octal1 = str(rem) + octal1      # octal1 stores the octal number with zeroes. i.e. '0o00003932' etc.
    numo //= 8      # numo stores the next number to be divided by 8
for l in octal1:
    if octal != '0o':   # This loop works to remove those zeroes in the start
        octal += l
        continue        # like j, l here checks which zero is needed and which is not
    elif l != '0':
        octal += l      # The final answer is stored in octal
    else:
        continue
print(f'The octal equivalent of {num}: {octal}')    # To display num here, I avoided changing its value in the process
