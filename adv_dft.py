from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
# print(f"room graph / {room_graph}")

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

traversal_graph = {}
for i in room_graph:
    traversal_graph[i] = room_graph[i][1]
print(f'traversal graph / {traversal_graph}')

# ---------------------------------------------------
            # DFT Procedure 
# ---------------------------------------------------
# Create a queue/stack as appropriate
# Put the starting point in that
# Make a set to keep track of where we’ve been
# While there is stuff in the queue/stack
#    Pop the first item
#    If not visited
#       DO THE THING!
#       Add to visited
#       For each edge in the item
#           Add that edge to the queue/stack


# ---------------------------------------------------
            # README Procedure 
# ---------------------------------------------------
# pick a random unexplored direction from the player's current room
# travel and log that direction
# loop
# take shortest path to room with unexplored paths ( utilizes bft?)



# ---------------------------------------------------
            # Traversal Graph
# ---------------------------------------------------
# # def bft():
# stack = Stack() # Create a queue/stack as appropriate
# stack.push(player.current_room.id) # Put the starting point in that
# visited_rooms = set() # Make a set to keep track of where we’ve been
# player.current_room = world.starting_room

# while stack.size() > 0: # While there is stuff in the queue/stack
#     curr_room = stack.pop() # Pop the first item
    
#     if curr_room not in visited_rooms: # If not visited
#         # DO THE THING! Implement README Procedure
        
#         exits = player.current_room.get_exits()
#         # pick a random unexplored direction from the player's current room
#         new_direction = exits[random.randint(0, len(exits) - 1)]
#         print(f"new direction / {new_direction}") # island Problem? 
#         traversal_path.append(new_direction)  # travel and log that direction
#         visited_rooms.add(curr_room)
#         for move in traversal_path:
#             player.travel(move)
#             stack.push(player.current_room.id)

#         # TODO take shortest path to room with unexplored paths ( utilizes bft?)
#         # maybe convert above for loop into bft 


# ---------------------------------------------------
            # Traversal DFT w/ Search BFT
# ---------------------------------------------------
# dft with bfs for next empty room 
#

stack = Stack() # Create a queue/stack as appropriate
que = Queue()

# Put the starting point in that
# Starting point in coordinate form ( 0, 0)
room_coord = room_graph[player.current_room.id][0]
stack.push(player.current_room.id) 
visited_rooms = set() # Make a set to keep track of where we’ve been
# player.current_room = world.starting_room

while stack.size() > 0: # While there is stuff in the queue/stack
    curr_room = stack.pop() # Pop the first item
    
    if curr_room not in visited_rooms: # If not visited
        # DO THE THING! Implement README Procedure
        
        exits = player.current_room.get_exits()
        # pick a random unexplored direction from the player's current room
        new_direction = exits[random.randint(0, len(exits) - 1)]
        print(f"new direction / {new_direction}") # island Problem? 
        traversal_path.append(new_direction)  # travel and log that direction
        visited_rooms.add(curr_room)
        for move in traversal_path:
            player.travel(move)
            stack.push(player.current_room.id)
            
            que.enqueue(player.current_room.id) #Begin BFS for unvisited rooms
            while que.size > 0: 
                room_curr = que.dequeue()
                if room_curr not in visited_rooms:
                    #travel to that room 

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

# ---------------------------------------------------
            # Player Methods Test
# ---------------------------------------------------

# print(f"stack / {stack}")
# print(f"player current room / {player.current_room}")
print(f"player current room id / {player.current_room.id}")
print(f"player current room exits / {player.current_room.get_exits()}")

# bft()

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
