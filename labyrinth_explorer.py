import sys
def load_labyrinth(filename):
    
    with open(filename, "r") as f:
        lines = f.readlines()

    labyrinth = [list(line.strip()) for line in lines]
    return labyrinth

def dijkstra(labyrinth):
    wall = make_wall(labyrinth)
    start = find_position(labyrinth, "S")
    end = find_position(labyrinth, "E")
    pointer = start
    nearest = nearest_neighbours(walls, pointer)
    visited = [start]
    cost_list = []
    for position in nearest:
        cost = travel_cost(labyrinth, position)
        neighbour = [position, cost, pointer]
        cost_list.append(neighbour)
        visited.append(position)
    for cost in cost_list:
        print(cost[1])
    # point = cost_list.index(min(cost_list))
    # visited.append(nearest[point])           
    return cost_list

def size_of_labyrinth(labyrinth):
    return len(labyrinth), len(labyrinth[0])

def find_position(labyrinth, char):
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[0])):
            if labyrinth[i][j] == char:
                return i, j
            
def nearest_neighbours(walls, position):
    up = (position[0] - 1, position[1])
    down = (position[0] + 1, position[1])
    left = (position[0], position[1] - 1)
    right = (position[0], position[1] + 1)
    nearest =[up, down, left, right]
    for i in range(len(nearest)-2):
        if nearest[i] in walls:
            nearest.remove(nearest[i])
    return nearest
            
def travel_cost(labyrinth, position):
    if labyrinth[position[0]][position[1]] == "M":
        return 5
    elif labyrinth[position[0]][position[1]] == ".":
        return 1
    
    
def make_wall(labyrinth):
    walls = []
    for i in range(len(labyrinth)):
        for j in range(len(labyrinth[0])):
            if labyrinth[i][j] == "#":
                walls.append((i, j))
    return walls

labyrinth = load_labyrinth("labyrinth_5x5.txt")
walls = make_wall(labyrinth)
nearest = nearest_neighbours(walls, (1, 1))
print("Nearest:", nearest)

print(walls)
print("Labyrinth loaded:")
print(labyrinth)
cost = dijkstra(labyrinth)
print(f"Shortest path has a cost of: {cost}")