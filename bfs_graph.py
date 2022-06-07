'''
BFS algorithm in Python
Explore all the immediate neighbours first then continue to explore all the immediate neighbours of them
Use a Queue to keep track of paths/nodes to explore. Explore nodes in the order they were added. 
Add start node to queue and visited list and repeat below:
- Get current node by removing from front of the queue and print as BFS path node.  
- Append all neighbours of current node to the queue, if not already visited (to avoid revisiting) and
- also add those nodes to the visited list
repeat until all the elements in the queue are removed
'''

import collections

# BFS algorithm
def bfs(graph, root):

    visited  = set()
    visited.add(root)
    
    queue = collections.deque([root])

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(vertex)

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph1 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    graph2 = {0: [1,4], 1:[0,2,3,4], 2:[1, 3], 3:[1,2, 4], 4:[0,1,3]}
    
    graph, root = graph1, 0
    print(F"Graph Adjacency List: \n {graph} \n")
    print(F"Following is Breadth First Traversal from {root}: ")
    bfs(graph, root)

    
    
