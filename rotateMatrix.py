__author__ = 'Igor Sorokin'
__email__ = 'igor.sorokin66@gmail.com'
__status__ = 'Completed'
'''
Problem:
Given an image represented by an NxN matrix,
rotate the matrix by 90 degrees.
Source:
Cracking the Code Interview 4ed Page 48 problem 1.6
'''

size_col = 10
size_row = 10
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

for offset_col in range(inner_squares):
    for offset_row in range(0 + offset_col, size_row - offset_col - 1):
        printMatrix()
        #ROTATION 1
        save = matrix[start_row + offset_row][end_col - offset_col]
        matrix[start_row + offset_row][end_col - offset_col] = matrix[offset_col][offset_row]
        printMatrix()
        #ROTATION 2
        save2 = save
        save = matrix[end_row - offset_col][end_col - offset_row]
        matrix[end_row - offset_col][end_col - offset_row] = save2
        printMatrix()
        #ROTATION 3
        save2 = save
        save = matrix[end_row - offset_row][start_col + offset_col]
        matrix[end_row - offset_row][start_col + offset_col] = save2
        printMatrix()
        #ROTATION 4
        matrix[start_row + offset_col][start_col + offset_row] = save