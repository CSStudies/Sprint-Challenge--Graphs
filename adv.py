from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Stack, Queue

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph ={}

reverse_dir = {'n':'s', 's':'n', 'e':'w', 'w':'e'}
turn_right = {'n':'e', 's':'w', 'e':'s', 'w':'n'}

path = []

def dbt():
    traversal_graph[player.current_room.id] = player.current_room.get_exits()
    # random.shuffle(traversal_graph[player.current_room.id]) 
    
    # Check against main graph
    while len(traversal_graph) < len(room_graph) -1:
        print(f'Traversal Graph: {traversal_graph}')
        print(f'Traversal Path: {traversal_path}')
        print(f'Path: {path}')
        

        #if not in traversal graph
        if player.current_room.id not in traversal_graph:
            traversal_graph[player.current_room.id] = player.current_room.get_exits()
            random.shuffle(traversal_graph[player.current_room.id])

            dir = path[-1]
            traversal_graph[player.current_room.id].remove(dir)

        #if reached all rooms. pop from path, add to graph, then move
        while len(traversal_graph[player.current_room.id]) < 1:
            dir = path.pop()
            traversal_path.append(dir)
            player.travel(dir)

        move = traversal_graph[player.current_room.id].pop(0)
        print(f'Move: {move}')
        traversal_path.append(move)
        path.append(move)
        player.travel(move)

dbt()

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# if __name__=="__main__":
#     dft(player.current_room.id)


# def dft_recursive(starting_vertex, visited=None):

#         if visited is None:
#             visited = set()
#         visited.add(starting_vertex)
#         print(f'DFT_Visited: {visited}')
#         traversal_graph[starting_vertex] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
        
#         for exit in player.current_room.get_exits():
#             next_id = player.current_room.get_room_in_direction(exit).id
#             traversal_graph[player.current_room.id][exit] = next_id
#             print(f'Traversal Graph: {traversal_graph}')
#             if next_id not in visited:
#                 traversal_path.append(exit)
#                 print(f'Path: {traversal_path}')
#                 player.travel(exit)
#                 dft_recursive(next_id, visited)
#             elif next_id is None:
#                 print(f'Go Back:{ reverse_dir[exit]}')
#                 player.travel(reverse_dir[exit])
#                 dft_recursive(next_id, visited)
                
                # Begins BFT bft(next_id, visited)
                # q = Queue()
                # q.enqueue(next_id)
                # while q.size() > 0:
                #     if next_id in traversal_graph:

                #     for exit in player.current_room.get_exits():
                #         edge = player.get_room_in_direction(exit).id
                        

# def dft(starting_vertex):
#     s = Stack()
#     s.push(starting_vertex)
#     visited = set()
#     # traversal_graph[starting_vertex] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
#     while s.size() > 0:
#         vert = s.pop()
#         if vert not in visited:
#             #add vert to visited and traversal graph
#             print(f'current vertex: {vert}')
#             visited.add(vert)
#             traversal_graph[vert] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
#             print(f'visited: {visited}')

#             #Choose random direction and add it traversal path
#             exit = player.current_room.get_exits()
#             dex = random.randint(0, len(exit)-1)
#             traversal_path.append(exit[dex])
#             print(f'Path: {traversal_path}')

#             #add new room to traversal graph 
#             traversal_graph[vert][traversal_path[-1]] = player.current_room.get_room_in_direction(traversal_path[-1]).id
#             print(f'Traversal Graph {traversal_graph}')

#             #travel to new room and add it to the Stack
#             player.travel(traversal_path[-1])
#             print(f'move {traversal_path[-1]} to {player.current_room.id}')
#             print(' ')
#             s.push(player.current_room.id)

#     #BFS for '?'
#     q = Queue()
#     q.enqueue([player.current_room.id])
#     q_visited = set()
#     while q.size() > 0:
#         path = q.dequeue()
#         vert = path[-1]
#         # traveled = []
#         if vert not in q_visited:
#             print(f'destinations: {traversal_graph[vert]}')
#             print(f'values: {traversal_graph[vert].values()}')
#             values = traversal_graph[vert].values()
#             # for value in values:
#             #     if value == '?':
#             #         print(f'bfs path: {path}')
#             #         # traveled = traversal_path[-1]
#             #         return path
#             for exit in player.current_room.get_exits():
#                 print(f'bfs edge: {player.current_room.get_room_in_direction(exit).id}')


                # exit_id = player.current_room.get_room_in_direction(exit).id
                
                
                # if traversal_graph[exit_id].values()

            # if vert == destination_vertex:
            #     print(f'BFS path: {path} ')
            #     return path
            # for edge in self.get_neighbors(vert):
            #     path_list = list(path)
            #     path_list.append(edge)
            #     q.enqueue(path_list)
    
    # q = Queue()
    # q.enqueue(player.current_room.id)
    # q_visited = set()
    # while q.size() > 0: 
    #     vert = q.dequeue()
    #     if vert not in q_visited:
    #         print(f'current vertex: {vert}')
    #         q_visited.add(vert)
    #         traversal_graph[vert] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    #         for exit in player.current_room.get_exits():
    #             print(f'exit {exit}')
    #             # print(f'BFT {traversal_graph[vert][exit]}')
    #             if traversal_graph[vert][exit] == '?':
    #                 traversal_path.append(exit)
    #                 print(f'Path: {traversal_path}')
    #                 player.travel(exit)
                    
    #                 print(f'move {exit} to {player.current_room.id}')
    #                 q.enqueue(player.current_room.id)
    #             else:
    #                 traversal_path.append(reverse_dir[traversal_path[-1]])
    #                 player.travel(reverse_dir[traversal_path[-1]])
                    



                


            # for exit in player.current_room.get_exits():
            #     next_id = player.current_room.get_room_in_direction(exit).id
            #     traversal_graph[player.current_room.id][exit] = next_id
            #     print(f'Traversal Graph: {traversal_graph}')
            #     s.push(next_id)
                # player.travel(exit)
                # traversal_path.append(exit)
                # print(f'Path {traversal_path}')


