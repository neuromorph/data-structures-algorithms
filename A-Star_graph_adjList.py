'''
A-Star Algorithm: 
It is an informed search algorithm to search optimum path between a starting point and a target and it can be used for 
traversal or path planning. It is a complete(will always find a solution if it exists) and optimal algorithm with a drawback of 
high space complexity O(b^d), where b = branching factor(avg num of children per node) and d = depth of search for shortest path
It can be seen as an extension of Dijkstra's algorithm. A* achieves better performance by using heuristics to guide its search.
Compared to Dijkstra's algorithm, the A* algorithm only finds the shortest path from a specified source to a specified goal, 
and not the shortest-path tree from a specified source to all possible goals.
A weighted graph is considered where each edge represents the cost of traversing that path.
At each iteration of its main loop, A* needs to determine which of its paths to extend. It does so based on the cost of the path 
and an estimate of the cost required to extend the path all the way to the goal. Specifically, A* selects the path that minimizes
    f(n) = g(n) + h(n)
where n is the next node on the path, g(n) is the cost of the path from the start node to n, and 
h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal.
The heuristic is problem specific e.g. euclidian distance and if it never overestimates that cost then A* gurantees optimal path.

A* use a priority queue to perform the repeated selection of minimum-(estimated)-cost nodes to expand. This priority queue 
is known as the open set or fringe. At each step of the algorithm, the node with the lowest f(x) value is removed from the queue, 
the f and g values of its neighbors are updated accordingly, and these neighbors are added to the queue. The algorithm 
continues until a removed node (thus the node with the lowest f value out of all fringe nodes) is a goal node.
--(Wiki)
'''

from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices, adjmap):
        self.v = num_of_vertices
        self.adjmap = adjmap
        self.visited = []

    def h(self, neighbor, target_vertex):
        ##estimate of cost from neighbor to target node using heuristic. Here assuming constant cost of 1
        if neighbor == target_vertex:
            return 0
        else:
            return 1
          
    def astar(self, start_vertex, target_vertex):
        ## D: dict of nodes with their dist to target = shortest distance of the node from the start node + heuristic of dist from the node to the target
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0 + self.h(start_vertex, target_vertex)
        
        ## Dpath: dict of nodes and their shortest Path from start node
        Dpath = {v:[] for v in range(self.v)}
        Dpath[start_vertex]=[start_vertex]
    
        pq = PriorityQueue()  # Priority Queue on distances from Start for the vertices
        pq.put((0, start_vertex)) 
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            
            if current_vertex == target_vertex:
                break
                
            self.visited.append(current_vertex)
    
            for neighbor, neighbor_cost in self.adjmap[current_vertex]:
                if neighbor not in self.visited:
                    old_cost = D[neighbor] 
                    new_cost = D[current_vertex] - self.h(current_vertex, target_vertex) + neighbor_cost + self.h(neighbor, target_vertex)
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
                        Dpath[neighbor] = Dpath[current_vertex] + [neighbor]
                        
        return D[target_vertex], Dpath[target_vertex]
        
        
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

start_vertex = 0
target_vertex = 9
D, Dpath = g.astar(start_vertex, target_vertex)
print(F"Cost from {start_vertex} to {target_vertex}: {D}\nPath from {start_vertex} to {target_vertex}: {Dpath}")
# [0: 0, 1: 4, 2: 11, 3: 17, 4: 9, 5: 22, 6: 7, 7: 8, 8: 11]
