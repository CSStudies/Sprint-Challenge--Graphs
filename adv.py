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
                        

def dft(starting_vertex):
    s = Stack()
    s.push(starting_vertex)
    visited = set()
    traversal_graph[starting_vertex] = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
    while s.size() > 0:
        vert = s.pop()
        if vert not in visited:
            print(f'current vertex: {vert}')
            visited.add(vert)
            print(f'visited: {visited}')
            exit = player.current_room.get_exits()
            traversal_path.append(exit[random.randint(0, len(exit)-1)])
            player.travel(traversal_path[-1])
            print(f'move to {player.current_room.id} from {traversal_path[-1]}')
            s.push(player.current_room.id)

            # for exit in player.current_room.get_exits():
            #     next_id = player.current_room.get_room_in_direction(exit).id
            #     traversal_graph[player.current_room.id][exit] = next_id
            #     print(f'Traversal Graph: {traversal_graph}')
            #     s.push(next_id)
                # player.travel(exit)
                # traversal_path.append(exit)
                # print(f'Path {traversal_path}')


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
dft(player.current_room.id)

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