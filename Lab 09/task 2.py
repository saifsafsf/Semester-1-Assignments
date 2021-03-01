matrix = eval(input('Enter a matrix: '))    # Taking input
matrix.sort(key = sum, reverse = True)      # Sort in descending order
print(f'The resulting matrix will be: {matrix}')
