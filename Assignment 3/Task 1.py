import Maxim
import Remove       # Importing modules
import Reverse
nums = input('Enter a natural number: ')    # Taking input
if int(nums) > 0:
    largest_num = str()     # Defining variable before using in line 9
    while nums != '':
        max_num = Maxim.maxim(nums)     # Using Maxim module
        largest_num = max_num + largest_num     # Storing in descending order
        nums = Remove.remove_max(max_num, nums)     # Removing the max_num for next iteration
    print(f'\nThe Largest Number possible: {int(largest_num)}')
    smallest_num = Reverse.reverse(int(largest_num))    # Reversing the largest number
    print(f'The Smallest Number possibe: {smallest_num}\n')
else:   # Natural Numbers only
    print('Invalid Input... Natural Numbers only.')
