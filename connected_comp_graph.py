'''
Find connected components of a graph and their count. 

For each unvisited node, traverse its entire connected component and list the nodes.

We will use DFS to traverse graph.
        DFS algorithm in Python:
        Starting from the source, select a neighbour and explore that path fully before coming back to select another neighbour.

'''

# DFS algorithm with recurssion
def dfsrec(graph, root, visited):
        comp = [root] # List of nodes in current graph component
        visited.add(root)
        
        def dfs(root): # Use DFS to traverse through all nodes in current component 
                for neighbour in graph[root]:
                        if neighbour not in visited:
                                visited.add(neighbour)
                                comp.append(neighbour)
                                dfs(neighbour)
                
        dfs(root)
        return comp

def connect_comp(graph):
        
        visited = set() # Global set of visited nodes
        con_comps = [] # List of connected components (with list of nodes in each comp) 
        
        for node in graph:
                if node not in visited:
                        con_comps.append(dfsrec(graph, node, visited))
                        
        print(F"Found {len(con_comps)} components: \n {con_comps}")

if __name__ == '__main__':
    graph1 = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4: [2]}
    graph2 = {0: [1], 1:[0,2,3], 2:[1, 3], 3:[1,2], 4:[5], 5:[4], 6:[]}
    graph3 = {1:[2,3], 2:[1,3,9], 3:[1,2], 4:[5], 5:[4,8], 6:[7], 7:[6], 8:[5,10], 9:[2], 10:[8]}
    
    graph = graph3
    print(F"Graph Adjacency List: \n {graph} \n")
    
    connect_comp(graph)
    
    
    
