marks = float(input('Enter your marks (out of 100): ')) # Taking Input
if marks >= 100:
    print('Invalid value.')
elif marks < 25:        # Checking the conditions
    print('You have a grade F.')
elif 25 <= marks < 45:
    print('You have a grade E.')
elif 45 <= marks < 50:
    print('You have a grade D.')
elif 50 <= marks < 60:
    print('You have a grade C.')
elif 60 <= marks < 80:
    print('You have a grade B.')
else:
    print('You have a grade A.')
