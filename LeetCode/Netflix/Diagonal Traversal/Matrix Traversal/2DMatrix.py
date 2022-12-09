# Given a 2d Matrix, print all elements of the given matrix in diagonal order

# Prints all elements of a given matrix in diagonal order
R = 5
C = 5
def diagonalOrder(arr, n, m):
	
	# we will use a 2D vector to
	# store the diagonals of our array
	# the 2D vector will have (n+m-1)
	# rows that is equal to the number of
	# diagonals
	ans = [[] for i in range(n + m - 1)]
	
	for i in range(m):
		for j in range(n):
			ans[i + j].append(arr[j][i])
	
	for i in range(len(ans)):
		for j in range(len(ans[i])):
			print(ans[i][j], end = " ")
		print()

# Driver Code
# we have a matrix of n rows
# and m columns
n = 5
m = 4

# Function call
arr = [[1, 2, 3, 4],[ 5, 6, 7, 8],[9, 10, 11, 12 ],[13, 14, 15, 16 ],[ 17, 18, 19, 20]]
diagonalOrder(arr, n, m)

