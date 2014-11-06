__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Solved- Problem from Cracking the Code Interview'

size_col = 5
size_row = 5
matrix = [[0 for x in range(size_col)] for y in range(size_row)]

def initializeMatrix():
    i = 1
    for col in range(size_col):
        for row in range(size_row):
            matrix[col][row] = i
            i += 1
initializeMatrix()

def printMatrix():
    for col in range(size_col):
        for row in range(size_row):
            print(matrix[col][row], end="\t")
        print()
    print()

inner_squares = 0
if size_col % 2 == 0:
    inner_squares = size_col // 2
else:
    inner_squares = (size_col-1) // 2

start_col = 0
start_row = 0
end_col = size_col-1
end_row = size_row-1

for col in range(inner_squares):
    for row in range(0 + col, size_row - col - 1):
        #ROTATION 1
        save = matrix[start_row + row][end_col - col]
        matrix[start_row + row][end_col - col] = matrix[col][row]
        printMatrix()
        #ROTATION 2
        save2 = save
        save = matrix[end_row - col][end_col - row]
        matrix[end_row - col][end_col - row] = save2
        printMatrix()
        #ROTATION 3
        save2 = save
        save = matrix[end_row - row][start_col + col]
        matrix[end_row - row][start_col + col] = save2
        printMatrix()
        #ROTATION 4
        matrix[start_row + col][start_col + row] = save
        printMatrix()