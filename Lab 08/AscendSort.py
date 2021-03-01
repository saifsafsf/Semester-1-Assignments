def ascend_sort(input_list):
    '''ascend_sort([x])
        Returns list sorted in ascending order.'''
    for i in range(1, len(input_list)):     # To iterate len(list)-1 times
        for j in range((len(input_list))-i):
            if input_list[j] > input_list[j+1]:     # Comparing two consecutive values
                interchange = input_list[j+1]
                input_list[j+1] = input_list[j]     # Sorting consecutive values in ascending order
                input_list[j] = interchange
    return input_list
