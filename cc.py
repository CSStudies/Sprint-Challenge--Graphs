# from room import Room
# from player import Player
# from world import World

# import random
from ast import literal_eval

from util import Stack, Queue

# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
room_graph=literal_eval(open(map_file, "r").read())

class Graph: 
      
    # init function to declare class variables 
    def __init__(self,init_graph): 
        # self.V = V # Graph Length
        
        # self.adj = [[] for i in range(V)] #return array for each item 
        self.init_graph = init_graph
        self.traversal_graph = {}
        self.traversal_path = []
        self.path = []
        self.visited = []
        self.edgeList = []

    def buildGraph(self, room_graph):
        for k in room_graph:
            self.traversal_graph[k] = room_graph[k][0]
        print(f'Traversal_graph: {self.traversal_graph}')

        # for k in self.traversal_graph: 
        #     x = self.traversal_graph[k][0]
        #     y = self.traversal_graph[k][1]
        #     self.addEdge(x,y)

    
    def buildEdgeList(self):
        for k in self.traversal_graph:
            self.edgeList.append(self.traversal_graph[k])
        print(f'Edge List: {self.edgeList}')
    
    # def dft(starting_vertex):
    #     while len(self.visited) < len(self.traversal_graph):
    #         pass
            

# Driver Code 
if __name__=="__main__": 
      
    # Create a graph given in the above diagram 
    # 5 vertices numbered from 0 to 4 
    g = Graph(len(room_graph))
    
    g.buildGraph(room_graph)
    g.buildEdgeList()
    # g.addEdge(3,5)
    # g.addEdge(3,6) 
    # g.addEdge(3,7) 
    # g.addEdge(4,5) 
    # g.addEdge(5,5) 
    # g.addEdge(3,4) 
    # g.addEdge(3,3) 
    # g.addEdge(2,5) 
    # g.addEdge(1,5) 
    # g.addEdge(1,4) 
    # g.addEdge(1,3) 
    # g.addEdge(2,3) 
    # g.addEdge(4,6) 
    # g.addEdge(5,6) 
    # g.addEdge(5,7) 
    # g.addEdge(2,6) 
    # g.addEdge(1,6)
    # g.addEdge(1,7) 
    
    # cc = g.connectedComponents() 
    # print("Following are connected components") 
    # print(cc) 
  

    #   def DFSUtil(self, temp, v, visited): 
  
    #     # Mark the current vertex as visited 
    #     visited[v] = True
  
    #     # Store the vertex to list 
    #     temp.append(v) 
  
    #     # Repeat for all vertices adjacent 
    #     # to this vertex v 
    #     for i in self.adj[v]: 
    #         if visited[i] == False:

    #             # Update the list 
    #             temp = self.DFSUtil(temp, i, visited) 
    #     print(f'Temp: {temp}')
    #     return temp 
  
    # # method to add an undirected edge 
    # def addEdge(self, v, w): 
    #     self.adj[v].append(w) 
    #     self.adj[w].append(v) 
  
    # # Method to retrieve connected components 
    # # in an undirected graph 
    # def connectedComponents(self): 
    #     visited = [] 
    #     cc = [] 
    #     for i in range(self.V): 
    #         visited.append(False) 
    #     for v in range(self.V): 
    #         if visited[v] == False: 
    #             temp = [] 
    #             cc.append(self.DFSUtil(temp, v, visited)) 
    #     return cc 
        
    # def path_components(self):
    #     pass

  