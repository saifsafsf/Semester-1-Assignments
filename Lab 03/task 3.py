side1 = int(input("About a triangle,\nEnter 1st side: "))
side2 = int(input("Enter 2nd side: "))  # Taking input
side3 = int(input("Enter 3rd side: "))
if side1 == 0:  # If input = 0
    print("Please enter non-zero integers.")
elif side2 == 0:
    print("Please enter non-zero integers.")
elif side3 == 0:
    print("Please enter non-zero integers.")
elif (side1**2) == (side2**2) + (side3**2):  # Checking the conditions.
    print("The given sides are of a Right Triangle.")
elif (side2**2) == (side3**2) + (side1**2):
    print("The given sides are of a Right Triangle.")
elif (side3**2) == (side1**2) + (side2**2):
    print("The given sides are of a Right Triangle.")
else:
    print("The given sides are not of a Right Triangle.")
