'''
Find (near) shortest path and cost between two nodes in a graph using BFS traversal. 
Assume undirected graph and uniform cost of 1 per edge. By nature of BFS traversal, 
as soon as the target node is discovered, it will be close to shortest path (though not guaranteed).

From the start node, use BFS traversal till destination node is reached. First path to get there is the desired path.

We will use BFS to traverse graph.
BFS algorithm:
        Explore all the immediate neighbours first then continue to explore all the immediate neighbours of them
        Use a Queue to keep track of paths/nodes to explore. Explore nodes in the order they were added. 
'''

import collections

class Graph:
    def __init__(self, adjmap):
        self.adjmap = adjmap
        self.queue = collections.deque()
        self.visited = set()
        self.bfspath = {} ## bfspath: dict of nodes and their shortest Path from start node
        
    # BFS Path algorithm
    def bfs_path(self, start, target):

        self.bfspath[start]=[start]
        self.visited.add(start)
        self.queue.append(start)

        while self.queue:
        
            current = self.queue.popleft()
            if current == target:
                return self.bfspath[target], len(self.bfspath[target]) - 1

            for neighbor in self.adjmap[current]:
                if neighbor not in self.visited:
                    self.visited.add(neighbor)
                    self.queue.append(neighbor)
                    self.bfspath[neighbor] = self.bfspath[current] + [neighbor]
                        
        return [], float('inf')

  

if __name__ == '__main__':
    graph1 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    graph2 = {0: [1], 1:[0,2,3], 2:[1, 3], 3:[1,2], 4:[5], 5:[4], 6:[]}
    graph3 = {1:[2,3], 2:[1,3,9], 3:[1,2,4], 4:[3,5,9], 5:[4,8], 6:[7], 7:[6,9], 8:[5,10], 9:[2,4,7], 10:[8]}
    
    graph = graph3
    print(F"Graph Adjacency List: \n {graph} \n")
    
    g = Graph(graph)

    start_vertex = 1
    target_vertex = 7
    path, cost = g.bfs_path(start_vertex, target_vertex)
    print(F"Cost from {start_vertex} to {target_vertex}: {cost}\nPath from {start_vertex} to {target_vertex}: {path}")
    
    
    
