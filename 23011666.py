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

#---------------------------------------------------------------------------
# This line defines a function named bfs that takes two parameters:
#graph (the tree structure) and start_node (the starting point for traversal)
def bfs(graph, start_node):
    
 # Initializes an empty list to keep track of the nodes that have been visited.
    visited = []
    
    #Initializes a deque with the start_node as the only element. 
    #This deque will be used to store the nodes that need to be visited in the correct order.
    queue = deque([start_node])

#Begins a loop that will continue as long as there are nodes in the queue.
    while queue:
        
        #Removes and returns the leftmost node from the queue, which is the next node to be processed.
        node = queue.popleft()
        
        # Checks if the node has not been visited yet to avoid processing the same node multiple times.
        if node not in visited:
            
            #Adds the node to the visited list, marking it as visited.
            visited.append(node)
            
            #Adds all the children of the node to the queue.
            #This ensures that BFS will visit nodes level by level.
            queue.extend(graph[node])
            
#Once the queue is empty, the function returns the visited list,
#which contains the order in which the nodes were visited.
    return visited

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
bfs_order = bfs(tree, 'A')
dfs_order = dfs(tree, 'A')

# Print the order of visit
print(f"BFS Order: {bfs_order}")
print(f"DFS Order: {dfs_order}")