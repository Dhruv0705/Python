def SExpression(nodes):

    # Initialize a boolean graph to keep track of relationships between nodes
    graph = [[False] * 26 for _ in range(26)]

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

    # Initialize the number of roots to 0
    numRoots = 0    
    # Initialize the root to ' '
    
    root = ' '

    # Check for E3, E4, or E5 errors

    for n in node:


        for i in range(26):


            if graph[i][ord(n) - ord('A')]:
                break
            

            
            if i == 25:
                numRoots += 1
                root = n

                if dfs(n, graph, [False] * 26):
                    return "E3"

    if numRoots == 0:
        return "E3"
    elif numRoots > 1:
        return "E4"
    elif root == ' ':
        return "E5"

    return helper(root, graph)

def addIntChar(x, c):
    return chr(x + ord(c))

def checkE1(graph):
    for i in range(26):
        count = 0

        for j in range(26):
            if graph[i][j]:
                count += 1

        if count > 2:
            return True

    return False

def checkE2(nodes, graph, node):
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
    if visited[ord(node) - ord('A')]:
        return True

    visited[ord(node) - ord('A')] = True

    for i in range(26):
        if graph[ord(node) - ord('A')][i]:
            if dfs(addIntChar(i, 'A'), graph, visited):
                return True

    return False

def helper(root, graph):
    l = ""
    r = ""

    for i in range(26):
        if graph[ord(root) - ord('A')][i]:
            l = helper(addIntChar(i, 'A'), graph)

            for j in range(i + 1, 26):
                if graph[ord(root) - ord('A')][j]:
                    r = helper(addIntChar(j, 'A'), graph)
                    break
            break

    return "(" + root + l + r + ")"
