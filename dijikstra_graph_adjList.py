'''
Dijikstra's Algorithm:
It is a graph search algorithm to find the shortest path between nodes of a graph. It can be used to find the shorest distance from 
a start node to all other nodes in the graph. 
A weighted graph is considered where each edge represents the cost of traversing that path.
At each iteration of its main loop, it needs to determine which of its paths to extend. It does so based on the cost of the path.
We use a priority queue to perform the repeated selection of minimum-cost nodes to expand. At each step of the 
algorithm, the node with the lowest cost is removed from the queue, the costs of its neighbors are updated accordingly
(if new cost through current node is less than old cost then replace old with new), and these neighbors are added to the queue. 
The algorithm continues until a removed node is a goal node.

'''

from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices, adjmap):
        self.v = num_of_vertices
        self.adjmap = adjmap
        self.visited = set()
       
    def dijkstra(self, start_vertex):
        ## D: dict of nodes and their shortest distances from start node
        D = {v:float('inf') for v in range(self.v)}  # Initially set to infinity and iteratively replace when lower-cost-paths are found. 
        D[start_vertex] = 0
        
        ## Dpath: dict of nodes and their shortest Path from start node
        Dpath = {v:[] for v in range(self.v)}
        Dpath[start_vertex]=[start_vertex]
    
        pq = PriorityQueue()  # Priority Queue on distances from Start for the vertices
        pq.put((0, start_vertex))
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.add(current_vertex)
    
            for neighbor, neighbor_weight in self.adjmap[current_vertex]:
                if neighbor not in self.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + neighbor_weight
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        Dpath[neighbor] = Dpath[current_vertex] + [neighbor]
        return D, Dpath
        
        
## test graph        
num_of_vertices = 10
##adjmap {node1:[(node2, weight12), (node3, weight13)]....
adjmap = { 0:[(1,4), (6,7)], 
                   1:[(0,4), (6,11), (7,20), (2,9)], 
                   2:[(1,9), (3,6), (4,2)], 
                   3:[(2,6), (4,10), (5,5)], 
                   4:[(2,2), (3,10), (5,15), (7,1), (8,5)], 
                   5:[(3,5), (4,15), (8,12)], 
                   6:[(0,7), (1,11), (7,1)], 
                   7:[(1,20), (4,1), (6,1), (8,3)],
                   8:[(4,5), (5,12), (7,3)],
                   9:[]  } 
       
g = Graph(num_of_vertices, adjmap)


D, Dpath = g.dijkstra(0)
print(F"Costs: {D}\nPaths: {Dpath}")
# [0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11, 9:inf]
