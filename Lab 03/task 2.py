num1 = int(input("Enter 1st integer: "))    # Taking input
num2 = int(input("Enter 2nd integer: "))
num3 = int(input("Enter 3rd integer: "))
# Finding the largest number
if num1 > num2:
    if num1 > num3:
    	print (f"{num1} is the largest number.")
    else:
    	print(f"{num3} is the largest number.")
elif num2 > num3:
    print(f"{num2} is the largest number.")
else:
    print(f"{num3} is the largest number.")
# Finding the smallest number
if num1 < num2:
    if num1 < num3:
        print (f"{num1} is the smallest number.")
    else:
        print(f"{num3} is the smallest number.")
elif num2 < num3:
    print(f"{num2} is the smallest number.")
else:
    print(f"{num3} is the smallest number.")
