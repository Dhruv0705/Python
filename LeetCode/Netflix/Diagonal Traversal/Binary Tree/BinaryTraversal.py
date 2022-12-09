# Python Program to print diagonal traversal using queue

# Tree Node
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None


def diagonalPrint(root):
	if root is None:
		return

	q = []
	q.append(root)

	while len(q) > 0:
		size = len(q)
		answer = []

		while size > 0:
			temp = q[0]
			q.pop(0)

			# traversing each component;
			while temp is not None:
				answer.append(temp.data)

				if temp.left is not None:
					q.append(temp.left)

				temp = temp.right

			size -= 1

		result.append(answer)


if __name__ == '__main__':
	root = Node(8)
	root.left = Node(3)
	root.right = Node(10)
	root.left.left = Node(1)
	root.left.right = Node(6)
	root.right.right = Node(14)
	root.right.right.left = Node(13)
	root.left.right.left = Node(4)
	root.left.right.right = Node(7)

	result = []

	diagonalPrint(root)

	for i in range(len(result)):
		for j in range(len(result[i])):
			print(result[i][j], end=" ")
		print()

