from collections import deque

# make our tree ready to work
tree = {
    'A': ['B', 'T'],
    'B': [ 'H'],
    'T': ['C','E'],
    'E': ['D', 'G'],
    'H': ['F'],
    'C': [],
    'G': [],
    'D': [],
    'F': []
}

#-----------------------------------------------------------------------------------------

#Defines a function named dfs that takes the same parameters as bfs.
def dfs(graph, start_node):
    
    #Initializes an empty list to keep track of the nodes that have been visited.
    visited = []
    
    #Initializes a list with the start_node as the only element.
    #This list will be used as a stack to store the nodes that need to be visited.
    stack = [start_node]

#Begins a loop that will continue as long as there are nodes in the stack.
    while stack:
        
        #Removes and returns the last node from the stack,
        #which is the next node to be processed in DFS.
        node = stack.pop()
        
        #Checks if the node has not been visited yet.
        if node not in visited:
            
            #Adds the node to the visited list.
            visited.append(node)
            
            # Adds all the children of the node to the stack.
            #The reversed function is used to maintain the correct order of traversal.
            stack.extend(reversed(graph[node]))

# Returns the visited list with the order of nodes visited in DFS.
    return visited

# call for the functions BFS and DFS with the instance (tree ,'A')
dfs_order = dfs(tree, 'A')

# Print the order of visit
print(f"DFS Order: {dfs_order}")
