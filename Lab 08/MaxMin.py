def maxmin(input_list):
    '''maxmin([x])
        Returns maximum & minimum numbers of the list'''    # Documentation
    max_num = input_list[0]     # Assigning first value as max
    for i in range(1, len(input_list)):
        if input_list[i] > max_num:     # Comparing every two consecutive values with each other
            max_num = input_list[i]
    min_num = input_list[0]     # Assigning first value as min
    for i in range(1, len(input_list)):
        if input_list[i] < min_num:     # Again, comparing two consecutive values
            min_num = input_list[i]
    return max_num, min_num     # Returning both vaues
