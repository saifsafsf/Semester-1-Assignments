def reverse(largest_num):
    '''reverse(int(x))
        Returns reversed int x'''   # Documentation
    smallest_num = 0    # Defining variable before using in line 7
    while largest_num != 0:
        rem = largest_num % 10
        smallest_num = smallest_num * 10 + rem
        largest_num //= 10      # Changing the value for next iteration
    return smallest_num
