num1 = int(input('Enter 1st natural number: '))
num2 = int(input('Enter 2nd natural number: '))     # Taking Input
if num1 > 0 and num2 > 0:
    if num1 > num2:
        max = num1
    else:
        max = num2
    for i in range(1, max+1):   # Finding H.C.F.
        if (num1 % i) == 0 and (num2 % i == 0):
            HCF = i
    LCM = (num1 * num2)/HCF     # Using formula
    print(f'L.C.M. of {num1} & {num2} is {LCM}')
else:
    print('Invalid Input...(Natural numbers only)')
