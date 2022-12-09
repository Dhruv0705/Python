# Given a two-dimensional array, 
# if any element within is zero, 
# make its whole row and column zero. 

# One naive solution which may come to the mind
# is to do a scan of the 2D matrix 
# and upon seeing a zero, 
# make that whole column and row zero. 
# But that is not correct; 
# even if there is only 1 zero in the matrix, 
# this will make the whole matrix zero.

# Instead, do a scan of the 2D array 
# and identify all the rows and columns 
# that have a zero in them and store 
# them in two sets.

import random
import copy

def create_random_matrix(rows, cols):
  v = []
  
  for i in range(0, rows):
    v.append([])
    for j in range(0, cols):
      t = random.randint(1, 100)
      v[i].append(t)
      if t <= 5:
        v[i][j] = 0
  return v

def print_matrix(m):
  print()
  for l in m:
    for x in l:
      print(x, end = '\t')
    print()
    

def make_zeroes(matrix):
  if not matrix:
    return

  zero_rows = set()
  zero_cols = set()

  rows = len(matrix)
  cols = len(matrix[0])

  for i in range(0, rows):
    for j in range(0, cols):
      if matrix[i][j] == 0:
        if i not in zero_rows:
          zero_rows.add(i)
        if j not in zero_cols:
          zero_cols.add(j)

  for r in zero_rows:
    for c in range(0, cols):
      matrix[r][c] = 0

  for c in zero_cols:
    for r in range(0, rows):
      matrix[r][c] = 0

def is_row_or_col_zero(matrix, r, c):
  if not matrix:
    return False

  rows = len(matrix)
  cols = len(matrix[0])

  for i in range(0, cols):
    if matrix[r][i] == 0:
      return True

  for i in range(0, rows):
    if matrix[i][c] == 0:
      return True

  return False

def verify(matrix):
  mat_copy = copy.deepcopy(matrix)
  make_zeroes(matrix)
  rows = len(matrix)
  cols = 0
  if rows > 0:
    cols = len(matrix[0])

  for i in range(0, rows):
    for j in range(0, cols):
      if is_row_or_col_zero(mat_copy, i, j):
        assert matrix[i][j] == 0
      else:
        assert matrix[i][j] != 0
          
      
def main():
  matrix = [
    [1, 5, 45, 0, 81],
    [6, 7, 2, 82, 8],
    [20, 22, 49, 5, 5],
    [0, 23, 50, 4, 92],
  ]
  print("Before: ")
  print_matrix(matrix)
  verify(matrix)
  print("After: ")
  print_matrix(matrix)
  matrix = create_random_matrix(5, 5)
  print("Before: ")
  print_matrix(matrix)
  verify(matrix)
  print("After: ")
  print_matrix(matrix)

main()

