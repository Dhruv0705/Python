def classGrouping(levels, maxSpread):
    # Initialize count to 1 since we always need at least one class
    count = 1
    
    # Sort the levels in ascending order
    levels.sort()
    
    # Initialize the current level to the first level in the list
    current = levels[0]
    
    # Loop through all the levels and check if a new class is needed
    for lvl in levels:

        # If the current level is more than maxSpread away from the previous level, a new class is needed
        if lvl > current + maxSpread:

            # Increment the count
            count += 1

            # Set the current level to the current level
            current = lvl
    
    # Return the count
    return count

def checkBST(root):
    def is_BST(root):
        if root == None:
            return True, None, None
        bool_left, min_left, max_left = is_BST(root.left)
        bool_right, min_right, max_right = is_BST(root.right)
        if bool_left and bool_right:
            if root.left==None and root.right==None:
                return True, root.data, root.data
            elif root.left==None and not root.right==None:
                if min_right>root.data:
                    return True, root.data, root.right
            elif not root.left==None and root.right==None:
                if max_left.data<root.data:
                    return True, min_left, root.data
            elif not root.left==None and not root.right==None:
                if max_left<root.data and min_right>root.data:
                    return True, min_left, max_right
        return False, None, None
    result, _, _ = is_BST(root)
    return result

def SExpression(nodes):
    # Initialize a boolean graph to keep track of relationships between nodes
    graph = [[False]*26 for _ in range(26)]
    # Use a set to store all unique nodes
    node = set()

    # Check for E2 error and populate graph and node set
    E2 = checkE2(nodes, graph, node)
    # Check for E1 error
    E1 = checkE1(graph)

    # If E1 error exists, return "E1"
    if E1:
        return "E1"
    # If E2 error exists, return "E2"
    elif E2:
        return "E2"

    # Check for E3, E4, or E5 errors
    numRoots = 0
    root = ' '
    for n in node:
        # For each node, check if it has any incoming edges
        for i in range(26):
            if graph[i][ord(n) - ord('A')]:
                break
            # If there are no incoming edges, increment numRoots and set root to the current node
            if i == 25:
                numRoots += 1
                root = n
                # Check for cycles using DFS
                if dfs(n, graph, [False]*26):
                    return "E3"

    # If there are no roots, return "E3"
    if numRoots == 0:
        return "E3"
    # If there are multiple roots, return "E4"
    elif numRoots > 1:
        return "E4"
    # If root is not set, return "E5"
    elif root == ' ':
        return "E5"

    # If there are no errors, generate S-Expression recursively
    return helper(root, graph)


def addIntChar(x, c):
    # Helper function to convert integer index to corresponding character
    return chr(x + ord(c))


def checkE1(graph):
    # Check for E1 error (a node has more than two incoming edges)
    for i in range(26):
        count = 0
        for j in range(26):
            if graph[i][j]:
                count += 1
        if count > 2:
            return True
    return False


def checkE2(nodes, graph, node):
    # Check for E2 error (duplicate edges)
    for i in range(1, len(nodes), 6):
        parent = ord(nodes[i]) - ord('A')
        child = ord(nodes[i + 2]) - ord('A')
        if graph[parent][child]:
            return True
        graph[parent][child] = True
        node.add(addIntChar(parent, 'A'))
        node.add(addIntChar(child, 'A'))
    return False


def dfs(node, graph, visited):
    # Depth-first search to check for cycles
    if visited[ord(node) - ord('A')]:
        return True
    visited[ord(node) - ord('A')] = True
    for i in range(26):
        if graph[ord(node) - ord('A')][i]:
            if dfs(addIntChar(i, 'A'), graph, visited):
                return True
    return False


def helper(root, graph):
    # Recursive function to generate S-Expression
    l = ""
    r = ""
    for i in range(26):
        if graph[ord(root) - ord('A')][i]:
            l = helper(addIntChar(i, 'A'), graph)
            for j in range(i

