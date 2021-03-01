def take_input(list_nums):      # For taking input in a list
    for counter in range(1, num+1):
        inputs = int(input(f'Enter number {counter}: '))
        list_nums.append(inputs)
    return list_nums

def removal(list_nums, list_nums2):     # For removing of the duplicate values
    for val in list_nums:
        if list_nums2.count(val) > 1:
            for i in range(1, list_nums.count(val)):
                list_nums2.remove(val)  # Storing the minimized list in list_nums2
    return list_nums2

def display_output(list_nums):      # To display output
    list_nums2.sort(key = list_nums.count, reverse = True)  # Sorting the list according to their frequency
    for j in list_nums2:
        if list_nums.count(j) > 1:
            print(f'{j} \t {list_nums.count(j)}')   # Valyes with frequency greater than 1

# Main Program

num = int(input('Enter number of values: '))    # Number of inputs in list
list_nums = []
list_nums = take_input(list_nums)   # Appending numbers in the list_nums
print('\nNumber \t Frequency')
list_nums2 = []
for a_num in list_nums:     # Making a duplicate of list_nums
    list_nums2.append(a_num)
list_nums2 = removal(list_nums, list_nums2)     # Removing duplicates
display_output(list_nums)       # Displaying output
print(f'\nThe list of numbers without duplicates: {list_nums2}')
