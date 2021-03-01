def maxim(nums):
    '''maxmin(str(x))
        Returns maximum item of the string'''    # Documentation
    max_num = nums[0]     # Assigning first value as max
    for i in range(1, len(nums)):
        if int(max_num) > int(nums[i]):     # Comparing every two consecutive values with each other
            max_num = nums[i]   # Updating max value if found a greater value
    return max_num
