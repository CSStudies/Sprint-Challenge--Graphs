from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

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
print(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
traversal_graph = {}

# ---------------------------------------------------
            # DFT from Notes
# ---------------------------------------------------
# def dft_recursive(self, starting_vertex, visited=None):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         This should be done using recursion.
#         """
#         if visited is None:
#             visited = set()
#         visited.add(starting_vertex)
#         print(starting_vertex)
#         for child_vert in self.vertices[starting_vertex]:
#             if child_vert not in visited:
#                 self.dft_recursive(child_vert, visited)
    

# ---------------------------------------------------
            # Traversal Graph
# ---------------------------------------------------
def recur(starting_room, visited_rooms=None):
    if visited_rooms is None: 
        visited_rooms = set()
    
    visited_rooms.add(starting_room.id)
    print(f'visited rooms / {visited_rooms}')
    traversal_graph[starting_room.id] = room_graph[starting_room.id][1]
    print(f'traversal graph / {traversal_graph}')
    exits = player.current_room.get_exits()
    print(f'exits / {exits}')

    opp_dir = {
        'n' : 's',
        's' : 'n',
        'e' : 'w',
        'w' : 'e'
    }

    for direction in exits:
        has_direction = player.current_room.get_room_in_direction(direction)
        if has_direction.id not in visited_rooms:
            # print(f'player.travel direction / {player.travel(direction)}')
            # if has_direction.id is None:
            #     continue
            # if len(exits) is 1:
            #     player.travel(exits[0])
            #     visited_rooms.add(player.current_room.id)
            #     traversal_path.append(exits[0])
            #     print(f'traversal path / {traversal_path}')
            #     recur(player.current_room, visited_rooms)
            
            player.travel(direction)
            visited_rooms.add(player.current_room.id)
            traversal_path.append(direction)
            print(f'traversal path / {traversal_path} \n')
            recur(player.current_room, visited_rooms)
        elif has_direction.id in visited_rooms:
            if len(exits) >= 1:
                player.travel(exits[random.randint(0, len(exits)-1)])
                visited_rooms.add(player.current_room.id)
                traversal_path.append(exits[0])
                print(f'traversal path / {traversal_path} \n')
                recur(player.current_room, visited_rooms)

        
        
        # elif has_direction.id is None or has_direction.id in visited_rooms:
        #     if direction is 'n':
        #         player.travel('s')
        #         traversal_path.append(direction)
        #         recur(player.current_room, visited_rooms)
        #     if direction is 's':
        #         player.travel('n')
        #         traversal_path.append(direction)
        #         recur(player.current_room, visited_rooms)
        #     if direction is 'e':
        #         player.travel('w')
        #         traversal_path.append(direction)
        #         recur(player.current_room, visited_rooms)
        #     if direction is 'w':
        #         player.travel('e')
        #         traversal_path.append(direction)
        #         recur(player.current_room, visited_rooms)


    # if traversal_graph[starting_room.id]['n'] is not '?' or None:
    #     player.travel('n')
    #     print(f'travel to room north / {player.current_room}')
    #     recur(player.current_room, visited_rooms)

    # if traversal_graph[starting_room.id]['s'] is not '?' or None:
    #     player.travel('s')
    #     print(f'travel to room south / {player.current_room}')
    #     recur(player.current_room, visited_rooms)

    # if traversal_graph[starting_room.id]['e'] is not '?' or None:
    #     player.travel('e')
    #     print(f'travel to room east / {player.current_room}')
    #     recur(player.current_room, visited_rooms)
        
    # if traversal_graph[starting_room.id]['w'] is not '?' or None:
    #     player.travel('w')
    #     print(f'travel to room west / {player.current_room}')
    #     recur(player.current_room, visited_rooms)

    

    # for room in traversal_graph:
    #     if room not in visited_rooms:
    #         recur(room, visited_rooms)


# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

        elif len(visited_rooms) == len(room_graph):
            print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
        else:
            print("TESTS FAILED: INCOMPLETE TRAVERSAL")
            print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

recur(player.current_room)


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
