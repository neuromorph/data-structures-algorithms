'''
DFS algorithm in Python:
Starting from the source, select a neighbour and explore that path fully before coming back to select another neighbour.
Use a Stack to keep track of paths/nodes to be explored. Explore last added node first.  
Add start node to the stack and a 'visited' list and repeat below:
- Get current node by popping from top of stack and print as DFS path node.  
- Push all neighbours of current node to the stack, if not already visited (to avoid revisiting) and
- also add those nodes to the visited list
repeat until all the elements in stack are popped
'''

import collections

# DFS algorithm with loop, without recurssion
def dfs(graph, root):

    visited  = set()
    visited.add(root)
    
    stack = collections.deque([root])

    while stack:
        #print(stack)
        # Dequeue a vertex from queue
        vertex = stack.pop()
        print(vertex)

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)

# DFS algorithm with recurssion
def dfsrec(graph, root):

        visited  = set()
        visited.add(root)
        
        def dfs(root):
                print(root)
                for neighbour in graph[root]:
                        if neighbour not in visited:
                                visited.add(neighbour)
                                dfs(neighbour)
        
        dfs(root)

if __name__ == '__main__':
    graph1 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    graph2 = {0: [1,4], 1:[0,2,3,4], 2:[1, 3], 3:[1,2, 4], 4:[0,1,3]}
    
    graph, root = graph1, 0
    print(F"Graph Adjacency List: \n {graph} \n")
    print(F"Following is Depth First Traversal from {root}: ")
    dfs(graph, root)
    print(F"Following is Depth First Traversal using Recurssion: ")
    dfsrec(graph, root)
    
    
