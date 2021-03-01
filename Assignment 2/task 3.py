num = int(input('Enter a number (from 1 to 50): '))     # Taking input
even_num = 0        # to start the second right triangle
if 0 < num < 51:    # if 51 or greater, the output will have 3 digit values, which ruins the pattern, like 99100101100
    for i in range(1, num+1):   # i for line number
        for j in range(num-i):      # j for space control
            print(end='   ')
        for k in range(i):      # k for first right triangle
            print('%3d' %(i+k), end='')
        for l in range(i-1):    # l for second right triangle
            print('%3d' %(even_num-l), end='')
        even_num += 2   # To increment its value for every new line
        print()     # Now, moving to next line
else:
    print('Invalid Input... Try entering a number between the limits mentioned.')

# The output is divided into 2 right triangles, one facing left & other to right.
# k & l refer to these right triangles.
