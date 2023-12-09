def flipping_matrix(matrix):
    row = col = len(matrix[0])
    sum = 0
    for i in range(0, row//2):
        for j in range(0, col//2):
            row1 = i
            row2 = row - i - 1
            col1 = j
            col2 = col - j - 1
            sum += max(max(matrix[row1][col1], matrix[row1][col2]),max(matrix[row2][col1], matrix[row2][col2]))
    return sum

matrix = [[112, 42, 83, 119], 
        [56, 125, 56, 49], 
        [15, 78, 101, 43], 
        [62, 98, 114, 108]] 
print(flipping_matrix(matrix))