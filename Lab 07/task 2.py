def custom_print(*inps, sep=' ', end='\n'):     # Defining function
    '''custom_print(x, y, z..., sep=', ', end='\\n')
        Acts exactly like print()'''    # Documentation
    len_inps = len(inps)
    for i, inp in enumerate(inps):
        print(f'{inp}', end='')
        if i < len_inps-1:      # len_inps-1 because index starts with 0
            print(f'{sep}', end='')
        if i == len_inps-1:
            print(f'{end}')
            
# Function will be called when run & is given arguments there.
