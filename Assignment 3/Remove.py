def remove_max(max_num, nums):
    '''remove_max(str(max_item), str(x))
        Removes the maximum item from string x'''   # Documentation
    nums2 = str()       # Emptying the string for the new string
    for num in nums:
        if num != max_num:      # All items will be added except largest one
            nums2 = num + nums2
        if num == max_num:      # largest item will be added if found multiple times
            max_num = None
    return nums2
